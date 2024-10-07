

# Fields

## Description

Fields are used to handle data in a manageable way.

They have the following properties:

- **Name** (optional): used to identify a field. Unnamed fields can also be used within records.
- **Value**: data we can handle through the field. Can be anything from numbers and text to more complex records.
- **Kind**: describe how the field itself can be used
- **Constraint**: a set of requirements that the value always satisfies. It is a combination of:
    - **Trait**: a record that defines what properties the value fundamentally has.
        For example, `Integer`{.oura}, `Real`{.oura} or `Text`{.oura}.
        More about this on the trait system pages.
    - **Purposes**: describe how the value can be used through this field 

## Usage

Here are a few key terms used when talking about fields:

- **Giving** a record to a field: making the given record the value of the field
- **Regiving** a record to a field: giving a record to a field that already has a value
- **Initialization** of a field: giving a record to a field that had no value before
- **Definition** of a field: initialization of a field that cannot be regiven to
- **Empty** field: field that has been declared and has constraints specified but is not initialized
- **Function** field: a field whose value is a *functor* record
    and that can be called with an argument to retrieve new fields.
    More on that on its own pages.
- **Modification* of a value: regiving to the value's sub-fields or modifying the sub-fields' values

```{.oura caption="A simple named field"}
** Here we give a value of 100 to the field 'score'
** the *name* of the field is 'score'
** the *value* of the field is number 100

score = 100

write! score ** prints '200'

```

No matter which value is given to the field, it never violates the trait constraint, 
nor can we use it in a way that violates its purpose constraint.
The constraints can be explicitly specified, or inferred from the field initialization.

```{.oura caption="Constraint violation"}
** First we give a value of 1 to the field 'a' with a 'Number' trait
** Then we give a value of "Monday" to the field 'b' with a 'Text' trait
** After we try to give a value of "Hello!" to the 'Number' field 'c',
** which violates its constraint

a: Number = 1 **OK

b: Text = "Monday" **Also OK

c: Number = "Hello!" **Error: Can't give a Text value to a Number field c
```

```{.oura caption="Regiving and constraints"}
** 'a' is first given value of 1, but regiven value of 2.
** it needs to be a variable for us to be able to regive it another value,
** which is specified by the 'var' keyword
** After we erroneously try to regive value of 4 to a field with a 'Text' trait

a var: Number = 1
a = 2                  **OK

b var: Text = "Monday"
b = 4                  **Error: Can't give a Number value to a Text field c
```

```{.oura caption="Inferrence and violation"}
** First we give a value of 1 to the variable field 'a', 
** without explicitly constraining it.
** Its trait constraint is inferred from the value given, which is an 'Integer'
** 'Integers' also have the 'Number' trait, so we could've made 'a' a 'Number'

a var = 1 **OK

a = "Hello!" **Error: Can't give a Text value to the Integer field a
```

## Kind

The field kind can be optionally specified during field declaration.
It describes whether the field owns its value and whether it can be regiven another one. More on the ownership and lifetime pages.

The 4 field kinds are **uniform**, **variable**, **reference** and **pointer**.
Which kinds own the value and which can be regiven one is described by the table:

|                          | Owns value | Doesn't own value |
| ------------------------ | ---------- | ----------------- |
| **Cannot be regiven to** | Uniform    | Reference         |
| **Can be regiven to**    | Variable   | Pointer           |

The kind is specified using one of the following keywords:

| Keyword       | Field kind  |
| ------------- | ----------- |
| `unif`{.oura} | A uniform   |
| `var`{.oura}  | A variable  |
| `ref`{.oura}  | A reference |
| `ptr`{.oura}  | A pointer   |

## Purposes

The purposes can also be optionally specified during field declaration and they also have defaults. 
These are the value purpose categories:

- **Mutability** - controls whether the field's value can be modified by accessing the field
    - **Constant** - the value's sub-fields cannot be modified, even if otherwise allowed by their own modes. *Default*
    - **Mutable** - the value's sub-fields can be modified, unless prevented by their own modes
- **Stability** - controls whether the field's value can be modified unexpectedly
    - **Stable** - the field's value can only be explicitly modified locally. *Default*
    - **Volatile** - the value might be modified inbetween times we use it locally, even if we aren't locally modifying it.
        Examples would be modifying the value from a different process/thread,
        changes in data from external devices, or any changes not covered by Oura's memory model.
        The value still satisfies the field's constraint.
- **Lifetime limit** - the maximum lifetime of the values.
    The value cannot be given to a field with a longer lifetime purpose.
    Note there's a difference between lifetime limits and value lifetimes.
    More on the ownership and lifetime pages.
    - **Localized** - the value only lives inside the embracing scope
        Ownership can only be *borrowed* by fields of shorter value lifespans 
        or *moved* to fields of equal value lifespans,
        *Default* for sub-fields.
    - **Outliving** - the value's lifetime is arbitrarily long.
        The ownership can be moved to any field.
        *Default* for function return fields.


The purposes are specified using special keywords that can be put in following categories:

| Purpose categories | Keywords                     | Default                  |
| ------------------ | ---------------------------- | ------------------------ |
| Mutability         | `const`{.oura}, `mut`{.oura} | constant                 |
| Stability          | /, `vol`{.oura}              | stable                   |
| Lifetime           | /, `liv out`{.oura}          | localized for sub-fields |

## Syntax

### Field specification

The field specification consists of its name (if it's a named field), its kind (unless default),
and its constraint separated by a colon (optional).
If the constraint is specified, either the purpose or trait (or both) has to be specied.
Default purposes can be ommited, and the trait is optional only if it can be inferred from its initialization.

```{.ouraspec caption="Syntax" }
«Identifier»⁽'name' optional⁾ «Kind_Keyword»⁽multiple⁾ ⁽⤹⁾: «Constraint»⁽⤸⁾⁽optional⁾
```

```{.ouraspec caption="Example" }
score var: Integer
```

If the field isn't named, at least one field kind keyword is mandatory.

### Constraints

```{.ouraspec caption="Syntax" }
«Purpose_Keyword»⁽more⁾ «Expression»⁽'trait'-optional⁾
```