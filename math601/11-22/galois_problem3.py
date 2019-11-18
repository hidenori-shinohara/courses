from sympy.polys.polyfuncs import symmetrize
from sympy import *
from sympy.polys.orderings import monomial_key

x, y, z = symbols('u_1 u_2 u_3')

s1 = x + y + z
s2 = x * y + y * z + z * x
s3 = x * y * z

v = x * y * y + y * z * z + z * x * x
vv = y * x * x + x * z * z + z * y * y


#print("Problem 3(iii)")
#print(expand(v + vv - s1 * s2))

print("Problem 3(v)")
print(symmetrize(v * vv))
print(expand(symmetrize(v * vv)[0] - (9*s3**2 + s3*s1**3 - 6*s3*s1*s2 + s2**3)))
