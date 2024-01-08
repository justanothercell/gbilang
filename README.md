# gbilang
A (joke) interpreter for university lecture pseudo code

# Quickstart
1. Create a new file containing the code and save it to `gcd.gbi`
```lua
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
