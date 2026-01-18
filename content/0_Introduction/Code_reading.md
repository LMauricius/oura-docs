# Code reading

## Examples
Code examples are used to better convey language concepts we introduced.
Notes are put in comments started with a hash symbol (`code # comment`{.oura}),
which are meant for humans and ignored by the compiler.

Comments start with a `#` and span until the end of the line.
Multiline comments are surrounded by `/*` and `*/` characters.

```{.oura caption="A Hello world example"}
# This is a 'Hello world!' example

# We need to write to console
import write with [target = Console module Io Std]

# The main program
main[args, import write] var => {
    write "Hello world!"
}
```

Most examples don't mention the *modules* or the *main function*.
Unless they mention those,
it is assumed the necessary modules are imported and the example code snippet is placed in the main function.
If you want to run them yourself, place them inside this code template:

```{.oura caption="The Oura docs example code template"}
import module Io Std
import (read, write) with [target = Console Io]

main[args, import (read, write)] => {
    # Insert example code snippet here
}
```

The exact meaning of all special words and symbols will be explained in other chapters.
For now, assume the code put into the main function can be run.

## Syntax specification
In these docs, the exact language syntax is defined alongside examples. 
Sometimes to simplify understanding the syntax we use one of the following markers:

- `⁽optional⁾`{.ouraspec} - The previous structure can, or may not be used
- `⁽more⁾`{.ouraspec} - The structure is optional, but can also repeat
- `⁽list⁾`{.ouraspec} - The structure is repeating, but each entry is separated by a comma, possibly followed by whitespace. All in a single line.
- `⁽linelist⁾`{.ouraspec} - The structure is repeating, but each entry is in its own line. Empty/whitespace lines are allowed inbetween for readability.

The parts of code are also often surrounded by marker-parentheses like this: `⁽⤹⁾code⁽⤸⁾`{.ouraspec}. These look like parentheses with arrows pointing down to the code. This is used to note that the markers apply to a longer part of code, like this: `some code ⁽⤹⁾some marked code⁽⤸optional⁾ some more code`{.ouraspec}

## Bracket types and names
We use the following kinds of brackets:

- `(` and `)`: round *parens* (parentheses)
- `[` and `]`: square *brackets*
- `{` and `}`: curly *braces*
- `<` and `>`: angular *chevrons*