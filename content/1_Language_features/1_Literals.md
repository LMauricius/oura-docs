# Literals

## Types of literals
Literal values are values written directly where they are used,
that don't depend on any other values.

There are numeric and textual literals.

## Examples

```{.oura caption="Integer number literal"}
42
```

```{.oura caption="Real number literal"}
3.141592
```

```{.oura caption="Text literal"}
"Hello world!"
```

## Numeric literals

Numeric literals are written using digits.
If they contain a decimal dot, their trait is `Real`{.oura}.
Otherwise, their trait is `Integer`{.oura}.

Optionally, numbers can have a prefix that specifies the numeric base it is written in.
No matter the base, decimal dot and exponent of the same base are supported.
Supported bases are:

| Base        | Prefix      | Digits allowed        | Example            |
| ----------- | ----------- | --------------------- | ------------------ |
| Decimal     | *No prefix* | 0-9                   | `103`{.oura}       |
| Binary      | `0b`        | 0 and 1               | `0b1001011`{.oura} |
| Octal       | `0o`        | 0-7                   | `0o742`{.oura}     |
| Hexadecimal | `0x`        | 0-9, A, B, C, D, E, F | `0xFF8E32`{.oura}  |

Hexadecimal digits of values 10-15 are written using letters A-F, which can be uppercase or lowercase.

Numbers can also be written using scientific notation by writing the exponent after the number.
For all bases the exponent starts with an underscore `_`,
followed by either `+` or `-` for positive and negative exponents and the exponent itself.
The exponent is always written as a decimal number, but the base of the power is the same as for the significand.

```{.oura caption="Scientific notation of a literal"}
avogadro = 6.02_+23
```

Numbers can also optionally have underscores between digits, for readability.
Unless it's the start of the exponent, underscores are ignored.

```{.oura caption="Underscores between digits"}
prize = 1_000_500_000
```

## Textual literals

Textual literals all have the trait `Text`{.oura}.
They are strings of characters used to build messages that will at some point
be shown to the user in a human-understandable form.
The characters themselves are stored using numeric codes according to UTF-8 text format.

*Normal text* is surrounded by either single `'` or double `"` quotes.
It cannot be split along multiple lines and cannot contain non-printable characters.
The quotes aren't included in the literal's characters, but everything inbetween is.
For special characters (eg. invisible or unsupported symbols) you can use escape sequences.

```{.oura caption="Text literals"}
helloText = 'Hello,'
worldText = "World!
write (helloText + worldText) # Writes 'Hello,world!'
```

*Escape sequences* start with a backslash `\`.
Each sequence represents a *single* character in the text.
The supported sequences are in the table below:

| Sequence      | Character                                                                |
| ------------- | ------------------------------------------------------------------------ |
| \\n           | Newline                                                                  |
| \\r           | Carriage return                                                          |
| \\t           | Horizontal tab                                                           |
| \\v           | Vertical tab                                                             |
| \\\\          | Backslash (literal backslash character)                                  |
| \\\'          | Apostrophe/single quote (doesn't end the text literal)                   |
| \\\"          | Double quote (doesn't end the text literal)                              |
| \\b           | Backspace                                                                |
| \\e           | Escape (UTF-8 character)                                                 |
| \\f           | Formfeed/page break                                                      |
| \\a           | Alert/beep/bell (used for some terminals)                                |
| \\*DDD*       | Character with numeric code written with decimal digits *DDD* (0-255)    |
| \\x*XX*       | Character with numeric code written with hexadecimal digits *XX* (00-ff) |
| \\u*XXXX*     | Unicode code point *XXXX* (0000-ffff), below \\x10000                    |
| \\U*XXXXXXXX* | Unicode code point *XXXXXXXX* (exactly 8 hex digits)                     |

```{.oura caption="Escape sequences in text"}
# Writes 'Regards,' and 'Oura's author' in two lines
write "Regards,\nOura's author"
```

*Raw text* starts with a double quote `"` immediately followed by a new line.
It is used for easier writing of text with special characters
when we don't want to use escape sequences.
It follows special rules:

- Escape sequences aren't supported. Backslash `\` just becomes the `\` character of the text literal.
- Each line of the text starts with a single quote `'` and spans until the end of the line in the code. All characters after the first `'` just become characters of the text, including quotes `'` and `"`.
- A line that starts with a `"` ends the raw text. It's not treated as an additional line of text literal.
- Whitespace before the first `'` or `#` is ignored, just as lines that contain only whitespace (empty lines).
- Multiple newlines (empty lines) just become a single newline of the text.
- Comments are supported and started using `#` instead of `'`. They span until the end of the line.
- Lines that start with anything besides `'`, `"` or `#` after the whitespace aren't allowed.

```{.oura caption="Raw text"}
myText = "
    'This is some long text...
    # This is a comment, inside the text literal!
    # Next we have another line of the literal:
    'We can have special characters in this text, like \, ', and ".
    '
    'Regards,
    'Oura's author.
    " # This is the end of a raw textual literal
```