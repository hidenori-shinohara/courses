from sympy import *

x = symbols('x')

f = 2 * x ** 2 - 6 * x + 28
g = 2 * x ** 2 / 3 - 3 * x / 5 + 7 * x ** 0 / 11
print("The content of %s is %s" % (f, content(f)))
print("The content of %s is %s" % (g, content(g)))
