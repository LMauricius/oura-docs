#!/bin/python3

import subprocess
import os
import re
import shutil
import sys
from pathlib import Path


# ---- Colored exceptions --------------------------------------------------------------------------


def set_highlighted_excepthook():
    import sys, traceback
    from pygments import highlight
    from pygments.lexers import get_lexer_by_name
    from pygments.formatters import TerminalFormatter

    lexer = get_lexer_by_name("pytb" if sys.version_info.major < 3 else "py3tb")
    formatter = TerminalFormatter()

    def myexcepthook(type, value, tb):
        tbtext = "".join(traceback.format_exception(type, value, tb))
        sys.stderr.write(highlight(tbtext, lexer, formatter))

    sys.excepthook = myexcepthook


set_highlighted_excepthook()

# ---- Terminal colors ----
Default = "\033[0m"
Black = "\033[30m"
Red = "\033[31m"
Green = "\033[32m"
Yellow = "\033[33m"
Blue = "\033[34m"
Magenta = "\033[35m"
Cyan = "\033[36m"
Gray = "\033[37m"
StrongBlack = "\033[30;1m"
StrongRed = "\033[31;1m"
StrongGreen = "\033[32;1m"
StrongYellow = "\033[33;1m"
StrongBlue = "\033[34;1m"
StrongMagenta = "\033[35;1m"
StrongCyan = "\033[36;1m"
StrongGray = "\033[37;1m"

# ---- Utilities -----------------------------------------------------------------------------------

def cleanName(fname: str) -> str:
    fname = os.path.splitext(os.path.basename(fname))[0]

    # Clean leading digits
    m = re.match(r"[0-9]+", fname)
    if m:
        fname = fname[m.end() :]

    # Clean underscores
    fname = fname.translate(fname.maketrans("_", " ")).strip()

    return fname


def safeName(name: str) -> str:
    return name.translate(name.maketrans(" ", "_")).lower()


# ---- Page structure ------------------------------------------------------------------------------


class Page:
    def __init__(self) -> None:
        self.file: str = ""
        self.subPages: dict[str, Page] = {}
        self.order: list[str] = []
        self.name: str = ""
        self.level: int = 0


def getSourceStructure(path: str, level: int = 0) -> Page:
    src = Page()
    src.name = cleanName(path)
    src.level = level

    if os.path.isdir(path):
        for subname in os.listdir(path):
            subpath = path + "/" + subname

            # order
            if os.path.basename(subpath) == "_order.txt":
                with open(subpath) as file:
                    for l in file.read().splitlines():
                        src.order.append(l)

            # main file
            elif cleanName(subpath) == src.name:
                src.file = subpath
            # sub pages
            elif os.path.isdir(subpath) or subpath.endswith(".md"):
                src.subPages[cleanName(subpath)] = getSourceStructure(
                    subpath, level + 1
                )
    else:
        src.file = path

    return src


# ---- Page building -------------------------------------------------------------------------------

def getHtmlContents(src: Page, urlPrefix="", index=0, indent=0, current="") -> str:
    ret = ""
    indentstr = 4 * indent * " "

    i = 0
    for s in src.order:
        i += 1

        if s in src.subPages.keys():
            subpage = src.subPages[s]

            if subpage.name.lower() == current.lower():
                ret += indentstr + f"<li><b>{str(i)} {subpage.name}</b>\n"
            elif subpage.file != "":
                ret += (
                    indentstr
                    + f'<li><a href="{urlPrefix+safeName(subpage.name)}.html">{str(i)}&nbsp{subpage.name}</a>\n'
                )
            else:
                ret += indentstr + f"<li>{str(i)}&nbsp{subpage.name}\n"

            if len(subpage.order) > 0:
                ret += indentstr + f"<ul>\n"
                ret += getHtmlContents(subpage, urlPrefix + "", i, indent + 1, current)
                ret += indentstr + f"</ul>\n"

            ret += indentstr + f"</li>\n"
        else:
            raise RuntimeError(
                f"{Red}Subpage '{Cyan}{s}{Default}' from '{Cyan}{src.file}{Red}' does not exist{Default}"
            )

    return ret


def buildHtmlChunks(
    src: Page,
    currentPage: Page,
    srcdir: str,
    builddir: str,
    syntaxDefs: "list[str]",
):
    # Convert current file
    if currentPage.file != "":
        outfilename = builddir + "/" + safeName(currentPage.name) + ".html"
        print(f"Checking chunk '{Cyan}{outfilename}{Default}'...")
        if (not os.path.exists(outfilename)) or os.path.getmtime(
            currentPage.file
        ) > os.path.getmtime(outfilename):
            # print(["pandoc", currentPage.file, "--to", "html", "--highlight-style", f"{builddir}/highlight.theme"] + [x for d in syntaxDefs for x in ("--syntax-definition", d)])
            result = subprocess.run(
                [
                    "pandoc",
                    currentPage.file,
                    "--to",
                    "html",
                    "--highlight-style",
                    f"{builddir}/highlight.theme",
                ]
                + [x for d in syntaxDefs for x in ("--syntax-definition", d)],
                stdout=subprocess.PIPE,
            )
            pageContent: str = result.stdout.decode("utf8")

            print(f"Generating chunk '{Cyan}{outfilename}{Default}'...")
            with open(outfilename, "w+") as outfile:
                outfile.write(pageContent)
                print(
                    f"{StrongGreen}Generated chunk '{Cyan}{outfilename}{StrongGreen}'{Default}"
                )
        else:
            print(f"{StrongGreen}Generating not needed{Default}")

    # convert sub pages
    for name, subpage in currentPage.subPages.items():
        buildHtmlChunks(src, subpage, srcdir, builddir, syntaxDefs)


def buildHtmlFile(templ: str, src: Page, infilename: str, outfilename: str):
    currentName = cleanName(infilename)
    tableOfContents = getHtmlContents(src, index=1, indent=2, current=currentName)

    with open(infilename, "r") as file:
        pageContent = file.read()

        htmlstr = templ
        htmlstr = htmlstr.replace("(TITLE)", currentName)
        htmlstr = htmlstr.replace("(MAIN_CONTENT)", pageContent)
        htmlstr = htmlstr.replace("(NAVIGATION_SIDEBAR)", tableOfContents)

        with open(outfilename, "w+") as outfile:
            outfile.write(htmlstr)


def main():
    contentdir = sys.argv[1]
    srcdir = sys.argv[2]
    targetdir = sys.argv[3]
    builddir = sys.argv[4]
    themestyle = sys.argv[5]

    # list syntaxdefs
    print(f"{StrongBlack}[Listing syntax definitions]{Default}")
    print(f"From '{Cyan}{srcdir + "/syntaxparsers"}{Default}'")
    syntaxDefs = []
    for subname in os.listdir(srcdir + "/syntaxparsers"):
        infilename = srcdir + "/syntaxparsers/" + subname
        if not os.path.isdir(subname):
            syntaxDefs.append(infilename)
            print(f"Using syntax parsing specification '{Cyan}{infilename}{Default}'")

    # save theme
    print(f"{StrongBlack}[Highlight theme]{Default}")
    print(
        f"Saving highlight style {StrongCyan}{themestyle}{Default} to '{Cyan}{builddir}/highlight.theme{Default}'"
    )
    result = subprocess.run(
        ["pandoc", "--print-highlight-style", themestyle], stdout=subprocess.PIPE
    )
    Path(builddir).mkdir(parents=True, exist_ok=True)
    with open(f"{builddir}/highlight.theme", "w+") as ofile:
        ofile.write(result.stdout.decode("utf8"))
    args = [
        "pandoc",
        f"--template={srcdir}/pandoc-template-syntax.css",
        srcdir + "/pandoc-used-syntax-blocks.md",
        "--highlight-style",
        f"{builddir}/highlight.theme",
        "-o",
        targetdir + "/syntax_style.css",
    ]
    for syntaxDef in syntaxDefs:
        args += ["--syntax-definition", syntaxDef]
    subprocess.run(args)

    # get source
    src = getSourceStructure(contentdir, -1)

    # Get template
    templ: str = ""
    Path(srcdir).mkdir(parents=True, exist_ok=True)
    with open(srcdir + "/template.html") as file:
        templ = file.read()

    # print(json.dumps(src, indent=4, sort_keys=True, default=lambda o: getattr(o, '__dict__', str(o))))
    # print(getHtmlContents(src, index = 1))

    # Check if the file structure has changed
    print(f"{StrongBlack}[Checking cached ToC]{Default}")
    print(f"from '{Cyan}{builddir + "/cached-contents.html"}{Default}'")
    unselectedContents = getHtmlContents(src, index=1, indent=2, current="")
    contentsUpdated = True
    if os.path.exists(builddir + "/cached-contents.html"):
        with open(builddir + "/cached-contents.html", "r") as file:
            if file.read() == unselectedContents:
                contentsUpdated = False
    if contentsUpdated:
        with open(builddir + "/cached-contents.html", "w+") as file:
            file.write(unselectedContents)

    if contentsUpdated:
        print(f"{Yellow}Contents changed, rebuilding all...{Default}")
    else:
        print(f"{StrongGreen}Contents haven't changed{Default}")

    # Build html files in /build dir
    print(f"{StrongBlack}[Building chunks]{Default}")
    buildHtmlChunks(src, src, srcdir + "/content", builddir, syntaxDefs)

    # Generate final html in target dir and copy needed files
    print(f"{StrongBlack}[Outputting html]{Default}")
    for subname in os.listdir(builddir):
        infilename = builddir + "/" + subname
        if (
            subname.endswith(".html")
            and subname != "cached-contents.html"
            and not os.path.isdir(subname)
        ):
            outfilename = targetdir + "/" + subname
            if (
                contentsUpdated
                or (not os.path.exists(outfilename))
                or os.path.getmtime(infilename) > os.path.getmtime(outfilename)
            ):
                print(f"Building '{Cyan}{outfilename}{Default}'")
                buildHtmlFile(templ, src, infilename, outfilename)

    # Copy needed files
    shutil.copy2(srcdir + "/style.css", targetdir + "/style.css")
    shutil.copy2(
        srcdir + "/syntax_style_override.css", targetdir + "/syntax_style_override.css"
    )


try:
    main()
except RuntimeError as e:
    print(e)
