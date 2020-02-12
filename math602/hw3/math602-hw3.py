from sympy import *
from sympy.abc import x, y

# Check if p2 divides p1.
def isdivisible(p1, p2):
    (q, r) = pdiv(p1, p2, order='lex')
    return degree(r, x) < 0 and degree(r, y) < 0


# Divide p by polynomials in ps
def divisionAlgorithm(p, ps):
    rem = poly(0, x, y, order='lex')
    qs = []
    for i in range(len(ps)):
        qs.append(poly(0, x, y, order='lex'))
    while p != 0:
        divided = False
        for i in range(len(ps)):
            if isdivisible(LT(p), LT(ps[i])):
                divided = True
                (q, r) = pdiv(p, ps[i], order='lex')
                p = r
                qs[i] = qs[i] + q
        if not divided:
            rem += LT(p)
            p = p - LT(p)
    print(latex(rem))
    for i in range(len(qs)):
        print(latex(qs[i]))


p = poly(x**7 * y**2 + x**3 * y**2 - y + 1, order='lex')
div1 = poly(x * y**2 - x, order='lex')
div2 = poly(x - y * y * y, order='lex')

divisionAlgorithm(p, [div1, div2])
print()
divisionAlgorithm(p, [div2, div1])
