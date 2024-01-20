# Objects

## Description

Objects are the most fundamental entities of Oura language.
They are used to contain data we need, bind related values,
perform various mathematical and procedural operations and actions on data.

In Oura, data, functions and modules are all objects. 

## Usage

The objects are only useful when they contain some properties, usually values.
The objects can be seen as 'wrappers' or 'groups' for related values,
and often correspond to real-life items, concepts, and structures.
The values contained in an object are called its *members*.

*Values* are holders of *data*, alongside properties that tell us how we can handle the values.
The *data* can be anything from numbers and text to more complex structures, 
but is always an object too.
When we set a value to hold an object, we say it has been *assigned* the object.
The first assignment that is done as soon as we declare a value is called *initialization*.
A value that has been declared and has constraints specified but is not initialized is called a *prototype* value. 

```{.oura caption="Numbers and objects"}
pointA = (x = 1.5, y = 2.4)
pointB = (x = 4.8, y = 6.2)
myRectangle = (
    topLeftCorner = pointA
    bottomRightCorner = pointB
)

write! y topLeftCorner myRectangle
** The above line prints 2.4
```

The members are usually named values, which helps us identify what their purpose is.
Some values can change over time, whether by assigning them with other data, or their data being modified.
For that reason it's helpful to specify a *constraint* for the value.
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

## Syntax

### Object literal
The object literals are written as a series of member declarations surrounded by parentheses (`(` and `)`).

```{.ouraspec caption="Structure" }
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

```{.ouraspec caption="Structure" }
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

```{.ouraspec caption="Structure" }
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

```{.ouraspec caption="Structure" }
: «Constraint_Qualifier»⁽more⁾ «Expression»⁽'required trait'-optional⁾
```

The constraint qualifiers can be put in the following groups:

| Qualifier group | Keywords                 | Default |
| --------------- | ------------------------ | ------- |
| Mutability      | `mut, unif`{.oura}       | uniform |
| Stability       | `vol, firm`{.oura}       | firm    |
| Evaluation      | `static, dynamic`{.oura} | dynamic |