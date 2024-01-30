# Objects

## Description

Objects are the most fundamental entities of Oura language.
They are used to contain data we need, bind related values,
perform various mathematical and procedural operations and actions on data.

In Oura, data, functions and modules are all objects. 

## Usage

The objects are only useful when they contain some  **values**.
The objects can be seen as 'wrappers' or 'groups' for related values,
and often correspond to real-life items, concepts, and structures.
The values contained in an object are called its *members*.

### Values

Values consist of:
- **Name** (optional): the name we use to identify a value. Objects can also have a number of unnamed values. Such objects are called **tuples**. 
- **Content**: can be anything from numbers and text to more complex structures. It is an object that the value holds.
- **Constraint**: a set of requirements that the content of the value always satisfies. It is a combination of:
    - **Required trait**: an object that the content always has traits of.
        For example, `Integer`{.oura}, `Real`{.oura} or `String`{.oura}.
        More about this on the trait system pages.
    - **Handle modes**: properties that describe what you an do with the value

When we set a value's content to an object, we say it has been **assigned** the object.
If we change the content to another object, that is a **reassignment**.
A special kind of assignment that cannot be **reassigned** is called a **definition**.
The first assignment that is done as soon as we declare a value is called **initialization**.
A value that has been declared and has constraints specified but is not initialized is called a **prototype** value. 

```{.oura caption="A named value"}
score var: Integer = 100

** the *name* of the value is 'score'
** the *content* of the value is number 100
** the *required trait* of the value is 'Integer' (a number without a fraction)
** it has a non-default handle mode of a 'variable', meaning we can reassign it

score = 200

write! score
** The above line prints '200' to screen
```

No matter which data is assigned to the value, it never violates the constraint.
The constraint can be explicitly specified, or inferred from the value initialization.

```{.oura caption="Constraint violation"}
a: Number = 1
a = 5 **This is OK

b: String = "Monday"
b = "Tuesday" **Also OK

c: Number = 2
c = "Six" **Error: Can't assign a String to a Number value c
```

```{.oura caption="Constraint violation (with trait inferrence)"}
a = 1
a = 5 **OK

b = "Monday"
b = "Tuesday" **OK

c = 2
c = "Six" **Error
```

### Member values

Values that are contained in an object are called **members** of that object.
That object is called a **master** of its members.

Declaring a member value also defines a **getter function** value in the master's surrounding context.
The getter function is assigned to a value of the same name as the member value.
Calling the getter function with the master as its argument returns the value of the member.
So if we have a local value `player` whose content (object) has a member `score`, 
we can handle the score value as `score player`{.oura}.
That should be read as "*the* score *of* player".
In this case the `score` is a member of the `player`s content,
but outside of it `score` is a getter function value.

```{.oura caption="Numbers and other objects"}
pointA def (x = 1.5, y = 2.4)
pointB def (x = 4.8, y = 6.2)
myRectangle def (
    topLeftCorner = pointA
    bottomRightCorner = pointB
)

** 2.4 is the content of the first 'y'
** y is a member value of the first point object
** the first point object is the content of 'pointA'
** a copy of the first point object is the content of 'topLeftCorner'
** topLeftCorner is a member of the rectangle object
** the rectangle object is the content of 'myRectangle' value
** here, x, y, topLeftCorner and bottomRightCorner are all getter functions

write! y topLeftCorner myRectangle
** The above line prints 2.4
```

All values are members of *something*, except for the **context** values.
It is only important for now to know that there is a **local context** at every place of the code,
whose members (a.k.a. the **local values**) can be handled by their name alone.
The local context can be handled with the `local`{.oura} keyword.

```{.oura caption="Local values"}
using module Io Std
using write with Console Io

main def() => {
    foo = 100

    ** 'foo' is a local value

    write! foo ** foo is handled just by its name 'foo'
               ** prints '100'

    write! foo local ** same as above, 'local' keyword handles the local context
                     ** prints '100'
}
```

## Syntax

### Object literal
The object literals are written as a series of member declarations surrounded by parens (`(` and `)`).

```{.ouraspec caption="Syntax" }
** Empty object:
()

** Singleline:
(«Member_Declaration»⁽list⁾)

** Multiline:
(
    ⁽⤹⁾«Member_Declaration»⁽list⤸linelist⁾
)
```

```{.oura caption="Example"}
** Empty object
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
** Complete declaration:
«Value_Specification» «Initialization»

** Prototype declaration:
«Value_Specification»

** Unnamed declaration: 
«Expression»
```

```{.oura caption="Example" }
** Object with complete declaration:
(score var: Integer = 100)

** Object with prototype declaration:
(score var: Integer)

** Object with unnamed declaration:
(100)
```

### Value specification

The value specification consists of its name (if it's a named value), its ownership qualifier (unless default),
and its constraint separated by a colon (optional if it can be inferred from its initialization).

```{.ouraspec caption="Syntax" }
«Identifier»⁽'name'-optional⁾ «Ownership»⁽optional⁾ «Constraint»⁽optional⁾
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

The default ownership is *constant* if prototype or initialized using a definition (`def`{.oura} symbol).
If initialized using an assignment (`=`{.oura} symbol), it is *variable* instead.

If the value isn't named, the ownership qualifier is mandatory.

### Constraint

```{.ouraspec caption="Syntax" }
: «Constraint_Qualifier»⁽more⁾ «Expression»⁽'required trait'-optional⁾
```

The constraint qualifiers can be put in the following groups:

| Qualifier group | Keywords                 | Default |
| --------------- | ------------------------ | ------- |
| Mutability      | `mut, unif`{.oura}       | uniform |
| Stability       | `vol, firm`{.oura}       | firm    |
| Evaluation      | `static, dynamic`{.oura} | dynamic |