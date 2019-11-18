from sympy.polys.polyfuncs import symmetrize
from sympy import *
from sympy.polys.orderings import monomial_key

for a in range(-10, 10):
    if a != 0 and -8 % a == 0:
        print("64 - 48 \cdot d = %d" % (a, 64 - 48 * a))

x, y, z = symbols('x y z')

a = -8
b = 12

disc = 256 * b**3 - 27 * a**4

print("h(y) = %s" % latex(expand(y*y - disc)))

a = 0
b = 0
c = 8
d = 12
print("g(y) = %s" % latex(expand(y*y*y - b*y*y + (a*c - 4*d)*y - (c*c + d*(a*a - 4*b)))))
