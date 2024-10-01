

# Fields

Fields are used to handle data in a manageable way.

They have the following properties:

- **Name** (optional): the name we use to identify a field. Unnamed fields can also be used within records.
- **Qualities**: properties that describe what you can do with the field itself
- **Content**: a record that the field holds. Can be anything from numbers and text to more complex structures.
- **Constraint**: a set of requirements that the content of the field always satisfies. It is a combination of:
    - **Trait**: an record that the content always has traits of.
        For example, `Integer`{.oura}, `Real`{.oura} or `String`{.oura}.
        More about this on the trait system pages.
    - **Content modes**: properties that describe what you can do with the content

Here are a few key terms used in relation to fields:

- **Assignment**: setting a fields's content to a record
- **Reassignment**: changing existing content to another record
- **Initialization**: the first assignment of a field
- **Definition**: initialization of a field that cannot be later reassigned
- **Empty** field: field that has been declared and has constraints specified but is not initialized
- **Function** field: a field whose content is a *functor* record
    and that can be called with an argument to retrieve new fields.
    More on that on its own pages.

```{.oura caption="A named field"}
score var: Integer <- 100

** the *name* of the field is 'score'
** the *content* of the field is number 100
** the *required trait* of the field is 'Integer' (a number without a fraction)
** it has a non-default ownership mode of a 'variable', meaning we can reassign it

score <- 200

write! score
** The above line prints '200' to screen
```

No matter which data is assigned to the field, it never violates the constraint.
The constraint can be explicitly specified, or inferred from the field initialization.

```{.oura caption="Constraint violation"}
a var: Number <- 1
a <- 5 **This is OK

b var: String <- "Monday"
b <- "Tuesday" **Also OK

c var: Number <- 2
c <- "Six" **Error: Can't assign a String to a Number field c
```

### Field modes

The field modes can be optionally specified during field declaration.
They have defaults if unspecified. 
These are the content modes' categories:

- **Ownership** - controls whether the field owns its content and whether it can be reassigned. More on the ownership and lifetime pages.
    - **Constant** - a field that owns its content and cannot be reassigned.
        The ownership *might* be shared with other constants, but it's unspecified whether two constants own the same record. *Default*
    - **Variable** - a field that uniquely owns its content and can be reassigned.
    - **Reference** - a field that doesn't own its content and cannot be reassigned
    - **Pointer** - a field that doesn't own its content and can be reassigned

### Content modes

The content modes can also be optionally specified during field declaration and they also have defaults if unspecified. 
These are the content modes' categories:

- **Mutability** - controls whether the field's content can be modified by accessing the field
    - **Uniform** - the content's members cannot be ressigned or modified, even if otherwise allowed by their own modes. *Default*
    - **Mutable** - the content's members can be reassigned and/or modified, unless prevented by their own modes
- **Stability** - controls whether the field's content can change on its own while we are not accessing it in the local context
    - **Firm** - the field's content cannot change, except by explicitly modifying it locally. *Default*
    - **Volatile** - the content might change inbetween times we access it, even if we aren't locally modifying it.
        Examples would be modifying the content from a different process/thread,
        changes in data from external devices, or any changes not covered by Oura's memory model.
        The content still satisfies the field's constraint, and can only be accessed according to Oura's memory model.
- **Scope limits** - whether the ownership can be transfered outside of the current scope
    - **Non-leaving** - content ownership can only be *borrowed* by fields of shorter lifespans 
        or *transferred* to fields of equal lifespans,
        except if those fields' content is *leaving*.
        *Default* for member fields.
    - **Leaving** - the ownership can be transferred to fields of longer lifespans.
        *Default* for function return fields.

### Field specification

The field specification consists of its name (if it's a named field), its field modes (unless default),
and its constraint separated by a colon (optional if it can be inferred from its initialization).

```{.ouraspec caption="Syntax" }
«Identifier»⁽'name' optional⁾ «Field_Mode»⁽multiple⁾ ⤹: «Constraint»⤸⁽optional⁾
```

```{.ouraspec caption="Example" }
score var: Integer
```

The ownership is specified one of the following qualifiers:

| Keyword        | Field name  |
| -------------- | ----------- |
| `const`{.oura} | A constant  |
| `var`{.oura}   | A variable  |
| `ref`{.oura}   | A reference |
| `ptr`{.oura}   | A pointer   |

If the field isn't named, a field mode qualifier is mandatory.

### Constraint

```{.ouraspec caption="Syntax" }
«Constraint_Qualifier»⁽more⁾ «Expression»⁽'required trait'-optional⁾
```

The constraint qualifiers can be put in the following groups:

| Qualifier group | Keywords                    | Default     |
| --------------- | --------------------------- | -------     |
| Mutability      | `unif`{.oura}, `mut`{.oura} | uniform     |
| Stability       | `firm`{.oura}, `vol`{.oura} | firm        |
| Scope           | /, `leav`{.oura}            | non-leaving |