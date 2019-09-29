from sympy import *

x = symbols('x')

f = 3 * x ** 3 - 15 * x ** 2 - 21

constants = [1, -1, 7, -7]

for constant in constants:
    g = x + constant
    d, r = div(f, g, domain=QQ)
    print("f(x) = (%s) * (%s) + (%s)" % (latex(d), latex(g), latex(r)))

