from sympy import *

x = symbols('x')

f = x ** 3 + 4 * x ** 2 - 3 * x + 6

for constant in range(-10, 10):
    if constant != 0 and 6 % constant == 0:
        g = x + constant
        d, r = div(f, g, domain=QQ)
        print("f(x) &= (%s)(%s) + %s, \\\\" % (latex(d), latex(g), latex(r)))

