# gbilang
[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Open Source Love svg1](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://github.com/ellerbrock/open-source-badges/)
[![Awesome Badges](https://img.shields.io/badge/badges-awesome-green.svg)](https://github.com/Naereen/badges)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
![Repo size](https://img.shields.io/github/repo-size/DragonFighter603/gbilang)

A (joke) interpreter for university lecture pseudo code made to run pseudo code from university lectures on the subject 
_Basic Vocabulary of Computer Science_ (_Grundbegriffe der Informatik_, aka GBI).

# Quickstart
1. Create a new file containing the code and save it to `gcd.gbi`
```py
# computes the gratest common divisor (gcd) of two numbers a and b
a <- 10
b <- 15

while a != b do
    if a > b then
        a <- a - b
    else
        b <- b - a
    fi
od
return a
```
2. Run the program:
  - jit compiled: `py gbilang.py gcd.gbi`
  - compiled to python: `py gbilang.py -o gcd.py & py gcd.py`

# Documentation
## Variables
Variables are implictily created and can be any ascii alphabetic character.
Other variable names, especially multi-character ones are **undefined behavior**
## Expressions
```py
<expression> := { (<expression>) | <operation> | <variable> | <value> }
<variable> := { a-z | A-Z }
<value> := { 0-9 }+ {.}? { 0-9 }*
<operation> := <expression> + <expression> | <expression> - <expression> | <expression> * <expression> | <expression> / <expression>
```
Note that * and / has precedence over + and -
## Statements
### Assignment
```py
<var> <- <expression>
```
### If
```py
if <condition> then
    <body>
fi
```
#### With Else
```py
if <condition> then
    <then_body>
else:
    <else_body>
fi
```
### While
```py
while <condition> do
    <body>
od
```
### For [NOT YET SUPPORTED]
(nightly feature)
```py
for <variable> <- <start> to <end> do
    <body>
od
```
### Return
Return can be used to exit the program
```py
return <expression>
```
