from sympy.polys.polyfuncs import symmetrize
from sympy import *

x, y, z = symbols('u_1 u_2 u_3')

s1 = x + y + z
s2 = x * y + y * z + z * x
s3 = x * y * z

u = [x, y, z]

d = 0 * x + 1
for j in range(len(u)):
    for i in range(j):
        d *= (u[i] - u[j]) * (u[i] - u[j])

sym = symmetrize(d, formal = True)[0]

print(latex(sym))
