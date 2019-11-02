from sympy import *

x = symbols('x')

f = 1

def irreducible(b, c, p):
    for x in range(p):
        if (x * x + b * x + c) % p == 0:
            return False
    return True

p = 2



for b in range(p):
    for c in range(p):
        if irreducible(b, c, p):
            f = f * (x * x + b * x + c)
print(f)
print(expand(f))
