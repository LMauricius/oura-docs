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
If they contain a decimal dot, their known trait is `Real`{.oura}.
Otherwise, their known trait is `Integer`{.oura}.

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