# Records

## Description

Records are the building blocks of Oura programming.
They are used to contain data we need, group related values,
or to extend mathematical and procedural functionalities of the language.

In Oura, data, functions and modules are all described by records. 

## Usage

The records are only useful when they have some  **values**, and they themselves are contained in values.
They are best viewed as 'wrappers' or 'groups' for related values,
and often correspond to real-life items, concepts, and structures.
The values grouped by a record are called its *members*.

### Values

Values are holders of records.

They consist of:

- **Name** (optional): the name we use to identify a value. Records can also have a number of unnamed member values.
- **Value modes**: properties that describe what you can do with the value itself
- **Content**: a record that the value holds. Can be anything from numbers and text to more complex structures.
- **Constraint**: a set of requirements that the content of the value always satisfies. It is a combination of:
    - **Required trait**: an record that the content always has traits of.
        For example, `Integer`{.oura}, `Real`{.oura} or `String`{.oura}.
        More about this on the trait system pages.
    - **Content modes**: properties that describe what you can do with the content

Here are a few key terms used in relation to values:

- **Assignment**: setting a values's content to a record
- **Reassignment**: changing existing content to another record
- **Initialization**: the first assignment of a value
- **Definition**: initialization of a value that cannot be later reassigned
- **Empty** value: value that has been declared and has constraints specified but is not initialized
- **Function** value: a value whose content is a *functor* record
    and that can be called with an argument to retrieve new values.
    More on that on its own pages.

```{.oura caption="A named value"}
score var: Integer <- 100

** the *name* of the value is 'score'
** the *content* of the value is number 100
** the *required trait* of the value is 'Integer' (a number without a fraction)
** it has a non-default ownership mode of a 'variable', meaning we can reassign it

score <- 200

write! score
** The above line prints '200' to screen
```

No matter which data is assigned to the value, it never violates the constraint.
The constraint can be explicitly specified, or inferred from the value initialization.

```{.oura caption="Constraint violation"}
a var: Number <- 1
a <- 5 **This is OK

b var: String <- "Monday"
b <- "Tuesday" **Also OK

c var: Number <- 2
c <- "Six" **Error: Can't assign a String to a Number value c
```

### Member values

A record is called a **group** of its members.

Declaring a member value also defines a **getter function** globally.
The getter function has the same name as the member value.
It accepts a single argument which the group holding this member satisfies,
and returns a reference value to the member's content when called. 

So if we have a local value `player` whose content has a member `score`, 
we can access the score's record as `score player`{.oura}.
That should be read as "*the* score *of* player".
In this case the `score` value is a member of the `player`s content record,
but outside of it `score` is a getter function value.

```{.oura caption="Member values and getters"}
pointA = (x = 1.5, y = 2.4)
pointB = (x = 4.8, y = 6.2)
myRectangle = (
    topLeftCorner = pointA
    bottomRightCorner = pointB
)

** 2.4 is the content of the first 'y'
** y is a member value of the first point record
** the first point record is the content of 'pointA'
** a copy of the first point record is the content of 'topLeftCorner'
** topLeftCorner is a member of the rectangle record
** the rectangle record is the content of 'myRectangle' value
** here, x, y, topLeftCorner and bottomRightCorner are all getter functions

write! y topLeftCorner myRectangle
** The above line prints 2.4
```

All values are members of *something*, except for the **context** values.
It is only important for now to know that there is a **local context** at every place of the code,
whose members (a.k.a. the **local values**) can be accessed by their name alone.
The local context can be accessed with the `local`{.oura} keyword.

```{.oura caption="Local values"}
use module Io Std
use write with Console Io

main = ProgramArgs mut vol => {
    foo = 100

    ** 'foo' is a local value

    write! foo ** foo is accessed just by its name 'foo'
               ** prints '100'

    write! foo local ** same as above, 'local' keyword accesses the local context
                     ** prints '100'
}
```

### Value modes

The value modes can be optionally specified during value declaration.
They have defaults if unspecified. 
These are the content modes' categories:

- **Ownership** - controls whether the value owns its content and whether it can be reassigned. More on the ownership and lifetime pages.
    - **Constant** - a value that owns its content and cannot be reassigned.
        The ownership *might* be shared with other constants, but it's unspecified whether two constants own the same record. *Default*
    - **Variable** - a value that uniquely owns its content and can be reassigned.
    - **Reference** - a value that doesn't own its content and cannot be reassigned
    - **Pointer** - a value that doesn't own its content and can be reassigned

### Content modes

The content modes can also be optionally specified during value declaration and they also have defaults if unspecified. 
These are the content modes' categories:

- **Mutability** - controls whether the value's content can be modified by accessing the value
    - **Uniform** - the content's members cannot be ressigned or modified, even if otherwise allowed by their own modes. *Default*
    - **Mutable** - the content's members can be reassigned and/or modified, unless prevented by their own modes
- **Stability** - controls whether the value's content can change on its own while we are not accessing it in the local context
    - **Firm** - the value's content cannot change, except by explicitly modifying it locally. *Default*
    - **Volatile** - the content might change inbetween times we access it, even if we aren't locally modifying it.
        Examples would be modifying the content from a different process/thread,
        changes in data from external devices, or any changes not covered by Oura's memory model.
        The content still satisfies the value's constraint, and can only be accessed according to Oura's memory model.
- **Scope limits** - whether the ownership can be transfered outside of the current scope
    - **Non-leaving** - content ownership can only be *borrowed* by values of shorter lifespans 
        or *transferred* to values of equal lifespans,
        except if those values' content is *leaving*.
        *Default* for member values.
    - **Leaving** - the ownership can be transferred to values of longer lifespans.
        *Default* for function return values.

## Syntax

### Record literal
The record literals are written as a series of member declarations surrounded by parens (`(` and `)`).

```{.ouraspec caption="Syntax" }
** Empty record:
()

** Singleline:
(«Member_Declaration»⁽list⁾)

** Multiline:
(
    ⁽⤹⁾«Member_Declaration»⁽list⤸linelist⁾
)
```

```{.oura caption="Example"}
** Empty record
()

** Singleline
(x=1, y=3)

** Multiline
(
    x=1, y=3
    z=5
)
```

### Member declaration

```{.ouraspec caption="Syntax" }
** Complete definition:
«Value_Specification» = «Expression»

** Complete non-constant initialization:
«Value_Specification» <- «Expression»

** Empty declaration:
«Value_Specification»

** Unnamed declaration: 
«Expression»
```

```{.oura caption="Example" }
** Record with initialization:
(score var: Integer <- 100)

** Record with empty declaration:
(score var: Integer)

** Record with unnamed value initialization:
(100)
```

### Value specification

The value specification consists of its name (if it's a named value), its value modes (unless default),
and its constraint separated by a colon (optional if it can be inferred from its initialization).

```{.ouraspec caption="Syntax" }
«Identifier»⁽'name' optional⁾ «Value_Mode»⁽multiple⁾ ⤹: «Constraint»⤸⁽optional⁾
```

```{.ouraspec caption="Example" }
score var: Integer
```

The ownership is specified one of the following qualifiers:

| Keyword        | Value name  |
| -------------- | ----------- |
| `const`{.oura} | A constant  |
| `var`{.oura}   | A variable  |
| `ref`{.oura}   | A reference |
| `ptr`{.oura}   | A pointer   |

If the value isn't named, a value mode qualifier is mandatory.

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