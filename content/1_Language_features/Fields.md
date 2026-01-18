

# Fields

## Description

Fields store values so we can identify, use and modify them.
They usually have a *name* (with rare exceptions) which refers to the field in the code.

```{.oura caption="A field" }
greeting = "Yo!"
write greeting # Writes 'Yo!'
```

Each field has the following: 

- **Name**: used to identify a field. Unnamed fields can also be used within tuples.
- **Value**: data we reach through the field. Can be anything from numbers and text to more complex records.
- **Ability**: a set of properties that tells us what we can do with that field.
    It is a combination of:
    - **Trait**: a record that defines what requirements the value always satisfies.
        For example, `Count`{.oura}, `Real`{.oura} or `Text`{.oura}.
        More about this on the trait system pages.
    - **Qualities**: describe how the value can be used through this field

## Usage



## Syntax

### Field specification

The field specification consists of its name (if it's a named field), its ownership mode (unless default),
and its constraint separated by a colon (optional).
If the constraint is specified, either the purpose or trait (or both) has to be specied.
Default purposes can be ommited, and the trait is optional only if it can be inferred from its initialization.

```{.ouraspec caption="Syntax" }
«Identifier»⁽'name' optional⁾ «Qualities» ⁽⤹⁾: «Expression»⁽'constraint'⁾⁽⤸⁾⁽optional⁾
```

```{.ouraspec caption="Example" }
score var: Integer
```

If the field isn't named, the field ownership keyword is mandatory.

### Qualities

Each quality can only appear once in the specification

```{.ouraspec caption="Syntax" }
⁽⤹⁾«Ownership»⁽or⁾«Volatility»⁽or⁾«Lifetime_limit»⁽⤸⁾⁽multiple⁾
```

```{.ouraspec caption="Example" }
currentTarget ref vol liv in targets: Integer
```

### Ownership 

```{.ouraspec caption="Syntax" }
const⁽or⁾var⁽or⁾ref⁽or⁾ptr
```

```{.ouraspec caption="Example" }
score var: Integer
PI const: Float64
```

### Volatility

```{.ouraspec caption="Syntax" }
⁽⤹⁾non vol⁽⤸⁾⁽or⁾⁽⤹⁾vol⁽⤸⁾
```

```{.ouraspec caption="Example" }
currentNode ref non vol: GraphNode
buttonCDown vol: Bool
```

### Lifetime limit

```{.ouraspec caption="Syntax" }
⁽⤹⁾in local⁽⤸⁾⁽or⁾⁽⤹⁾in «Expression_group»⁽⤸⁾⁽or⁾⁽⤹⁾out⁽⤸⁾
```

```{.ouraspec caption="Example" }
** TODO
```