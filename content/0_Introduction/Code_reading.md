# Code reading

## Examples
Code examples are used to better convey language concepts we introduced.
Notes are put in comments started with a double star (`code ** comment`{.oura}),
which are meant for humans and ignored by the compiler.

```{.oura caption="A Hello world example"}
** This is a 'Hello world!' example

** We need to write to console
use write with Console module Io Std

** The main program
main = ProgramArgs mut => {
    write! "Hello world!"
}
```

Most examples don't mention the so-called 'modules' or the 'main function'.
Unless they mention those things,
it is assumed the necessary 'modules' are used and the example code snippet is placed in the 'main function'.
If you want to run them yourself, place them inside this code template:

```{.oura caption="The Oura docs example code template"}
use module Io Std
use (read, write) with Console Io

main = ProgramArgs mut vol => {
    ** Insert example code snippet here
}
```

## Syntax definitions
In these docs, the language syntax is defined in code blocks. 
Sometimes, syntactic structures are not mandatory or can repeat, in which cases we use one of the following meta-markers:

- `⁽optional⁾`{.ouraspec} - The previous structure can, or may not be used
- `⁽more⁾`{.ouraspec} - The structure is optional, but can also repeat
- `⁽list⁾`{.ouraspec} - The structure is repeating, but each entry is separated by a comma, possibly followed by whitespace. All in a single line.
- `⁽linelist⁾`{.ouraspec} - The structure is repeating, but each entry is in its own line. Empty/whitespace lines are allowed inbetween for readability.

The parts of code are also often surrounded by meta-parentheses like this: `⁽⤹⁾code⁽⤸⁾`{.ouraspec}. They look like parentheses with arrows pointing down to the code. This is used to note that the meta-markers apply to a longer part of code, like this: `some code ⁽⤹⁾some marked code⁽⤸optional⁾ some more code`{.ouraspec}

## Bracket types and names
We use the following kinds of brackets:

- `(` and `)`: round *parens* (parentheses)
- `[` and `]`: square *brackets*
- `{` and `}`: curly *braces*
- `<` and `>`: angular *chevrons*