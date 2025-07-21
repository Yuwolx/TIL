# Control Statement

## Conditional statement (if, elif, else)
### if
- **expression: some literal line can express one value**
  - dust =  10 : it is expression
  - some(1,2) is expression cus can express '3'

- We write in conditional statement for expression
'''
if expression:
  codes
elif expression:
  codes
elif expression:
  codes
'''
- if match the condition then finish the codes

## Loop (for, while)
**practice use while alternate for**

### for
- Loop in sequence items in order
- Can write in loop condition that iterable objects

- element = [[a,b],[c,d]]
- If use inner list then use multile for statement

### while statement
**We have to write condtion in while statement**
- When variable cannot match condition then while statement will finish

#### List comprehension
['expression' for 'variable' in 'iterable']
list('expression' for 'variable' in 'iterable')
- iterable: have indecing sequence

### Loop control
finish, break ,,,

# Function
'''
def [function_name](varable_1,variable_2): #variables is parameter
  return v_1 + v_2
'''
- If you not write return valuse, then python return none

- 일급 객체
  - Function can assigned variable
  - Function can convey another function's variable
  - **Function have similer feature with int**

- **What is the parameter and argument**
  - When define function use parameter
  - When use function use 
    -  Any way, parameter and argument are different

## Arguments
### Positional Arguments
- Basically argument type

### Dafault Argument Values
- When define function can set default argument values
  - If user do not input argument, then python return dafault argument value

### Keyword Argument
### Arbitrary Argument lists
'''
def calculate_sum(*argument):
  codes
'''
- When use do not setting arguments size
  - couples argument cognitive tuple

### Arbitrart Keyword Argument Lists
def print_info(**kwargs):
- couples argument address dictionary

## Packing & Unpacking
- Unpacking *[list_name] 
- Can assigned each value in list to arguments

## Built in function
len max min sum avg
- use on for or while statement

### Lambda expression

## Styple Guide
Read in forder