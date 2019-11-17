from sympy import *
from sympy.polys.orderings import monomial_key

x, y, z = symbols('u_1 u_2 u_3')

s1 = x + y + z
s2 = x * y + y * z + z * x
s3 = x * y * z

v = x * y * y + y * z * z + z * x * x
vv = y * x * x + x * z * z + z * y * y


print(expand(v + vv - s1 * s2))

