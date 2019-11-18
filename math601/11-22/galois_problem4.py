from sympy.polys.polyfuncs import symmetrize
from sympy import *

u1, u2, u3 = symbols('u1 u2 u3')

u = [u1, u2, u3]

discriminant = 1
for i in range(3):
    for j in range(i + 1, 3):
        discriminant *= (u[i] - u[j]) * (u[i] - u[j])

print(latex(symmetrize(discriminant, formal = True)[0]))
