

# Control Statements

## Conditional Statements (`if`, `elif`, `else`)

### `if`

* **Expression: A literal line that can evaluate to a single value**

  * `dust = 10` → this is an expression
  * `some(1, 2)` is also an expression because it evaluates to `3`

* We write expressions inside conditional statements:

```python
if expression:
    codes
elif expression:
    codes
else:
    codes
```

* Once a condition matches, the corresponding code runs and the rest are skipped.

---

## Loops (`for`, `while`)

> **In practice, use `while` only when necessary—prefer `for` when looping over a sequence.**

### `for`

* Iterates over each item in a sequence (e.g., list, tuple, string)
* The loop condition can take any iterable object

Example:

```python
elements = [[a, b], [c, d]]
```

* If iterating over inner lists, we can use nested `for` statements

### `while`

* You must write a condition in a `while` loop
* The loop runs until the condition becomes false

---

### List Comprehension

```python
[expression for variable in iterable]
list(expression for variable in iterable)
```

* `iterable`: any object that can be iterated (e.g., list, string, etc.)
* More efficient and concise way to build a list

---

### Loop Control

* `break`: exit the loop early
* `continue`: skip to the next iteration
* `pass`: do nothing (used as a placeholder)

---

# Functions

```python
def function_name(parameter_1, parameter_2):
    return parameter_1 + parameter_2
```

* If you don’t write a `return` statement, Python returns `None` by default.

---

## First-Class Objects (일급 객체)

* Functions can be assigned to variables
* Functions can be passed as arguments to other functions
* **Functions are treated like data types (e.g., `int`)**

---

## Parameters vs. Arguments

* **Parameter**: the variable in the function definition
* **Argument**: the value passed to the function when it's called
  → They are related but not the same

---

## Positional Arguments

* The default way to pass arguments, based on their position

---

## Default Argument Values

* You can set default values for parameters in the function definition
  → If the user does not provide a value, the default is used

---

## Keyword Arguments

* You can pass arguments using the `parameter=value` format
  → This allows you to pass them in any order

---

### Arbitrary Argument Lists

```python
def calculate_sum(*args):
    codes
```

* Use `*args` when you don’t know how many arguments will be passed
* The arguments are received as a tuple

---

### Arbitrary Keyword Argument Lists

```python
def print_info(**kwargs):
    codes
```

* Use `**kwargs` to receive an arbitrary number of keyword arguments
* The arguments are received as a dictionary

---

## Packing & Unpacking

* `*list_name` → unpacks a list or tuple
* You can assign each value in a list to separate arguments in a function

---

## Built-in Functions

Common examples: `len()`, `max()`, `min()`, `sum()`

* Often used inside `for` or `while` loops

---

## Lambda Expressions

Anonymous, inline functions:

```python
lambda x, y: x + y
```

---

## Style Guide

Refer to the official Python style guide: **PEP 8**