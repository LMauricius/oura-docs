# Code reading

## Examples
Code examples are used to better convey language concepts we introduced. Notes are put in comments started with a double star (`code ** comment`{.oura}), which are meant for humans and ignored by the compiler.

```{.oura caption="A Hello world example"}
** This is a 'Hello world!' example

** We need to write to console
use write with Console (module Std)

** The main program
main def() => {
    write "Hello world!"
}
```

## Syntax definitions
In these docs, the language syntax is defined in code blocks. 
Sometimes, syntactic structures are not mandatory or can repeat, in which cases we use one of the following meta-markers:

- `⁽optional⁾`{.ouraspec} - The previous structure can, or may not be used
- `⁽more⁾`{.ouraspec} - The structure is optional, but can also repeat
- `⁽list⁾`{.ouraspec} - The structure is repeating, but each entry is separated by a comma, possibly followed by whitespace. All in a single line.
- `⁽linelist⁾`{.ouraspec} - The structure is repeating, but each entry is in its own line. Empty/whitespace lines are allowed inbetween for readability.

The parts of code are also often surrounded by meta-parentheses like this: `⁽(⁾code⁽)⁾`{.ouraspec}. This is used to note that the meta-markers apply to a longer part of code, like this: `some code ⁽(⁾some marked code⁽)optional⁾ some more code`{.ouraspec}