from sympy.polys.polyfuncs import symmetrize
from sympy import *

u1, u2, u3 = symbols('u_1 u_2 u_3')

u = [u1, u2, u3]

discriminant = 1
for j in range(len(u)):
    for i in range(j):
        discriminant *= (u[i] - u[j]) * (u[i] - u[j])

print(latex(symmetrize(discriminant, formal = True)[0]))
