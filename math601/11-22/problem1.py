from sympy import *
from sympy.polys.orderings import monomial_key

x, y, z, w = symbols('u1 u2 u3 u4')

f = (x * y + z * w) * (x * z + y * w) + (x * y + z * w) * (x * w + y * z) + (x * z + y * w) * (x * w + y * z) 
print(f)
print(latex(expand((x * y * z + x * y * w + x * z * w + y * z * w) * (x + y + z + w))))
print(expand((x * y * z + x * y * w + x * z * w + y * z * w) * (x + y + z + w) - f))
