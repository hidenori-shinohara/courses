from sympy import *

x = symbols('x')

def irreducible2(b, c, p):
    for x in range(p):
        if (x * x + b * x + c) % p == 0:
            return False
    return True

ps = [2, 3, 5, 7]

for p in ps:
    f = 1
    for b in range(p):
        f = f * (x - b)
        for c in range(p):
            if irreducible2(b, c, p):
                f = f * (x * x + b * x + c)
    print(trunc(f, p))

## Output is
# x**4 + x
# x**9 - x
# x**25 - x
# x**49 - x
