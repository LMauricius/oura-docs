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