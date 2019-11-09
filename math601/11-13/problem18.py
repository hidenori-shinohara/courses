from sympy import *
from random import *

x = symbols('x')

def randpoly(deg, mod):
    p = poly(0, x, modulus = mod)
    for d in range(deg):
        p = x * p + randint(0, mod - 1)
    return poly(p, x, modulus = mod)

# Find f^exp % modf in Z_{mod}
def polypow(f, exp, modf, mod):
    res = poly(1, x, modulus = mod)
    while exp > 0:
        if exp % 2 == 1:
            quotient, res = div(res * f, modf)
        quotient, f = div(f * f, modf)
        exp = exp // 2
    return res



def factor(f, p, originaldegree, factors, r):
    if f.degree() == r:
        factors.append(f)
    else:
        for i in range(30):
            h = randpoly(r, p)
            # Raise h to the power of (p^r - 1)/2.
            h = polypow(h, (p**r - 1) // 2, f, p)
            h = h - poly(1, x, modulus = p)
            d = gcd(f, h)
            if d.degree() == 0 or d.degree() == f.degree():
                continue
            else:
                # We found a proper factor.
                # Factorize further.
                factor(d, p, originaldegree, factors, r)
                quotient, remainder = div(f, d)
                factor(quotient, p, originaldegree, factors, r)
                return

def factorizepoly(f, mod):
    print("Factorize %s" % f)
    for r in range(1, f.degree() - 1):
        if f.degree() % r != 0: continue
        factors = []
        factor(f, mod, f.degree(), factors, r)
        if len(factors) * r != f.degree(): continue
        for fac in factors:
            print(latex(fac))
        print()
        return

f = poly(x**8 + x**7 - x**6 + x**5 + x**4 - x**3 - x**2 - x + 1, x, modulus = 3)
factorizepoly(f, 3)

f = poly((x**12+48*x**11+42*x**10+58*x**9+11*x**8+25*x**7+22*x**6+30*x**5+34*x**4+16*x**3+62*x**2+21*x+27), x, modulus = 73)
factorizepoly(f, 73)


f = poly((x**12+12*x**11 +25*x**10 + 40*x**9 + 6*x**8 + 15*x**7 + 24*x**6+ 42*x**5 + 8*x**4 + 48*x**3 +68*x**2 + 50*x +68), x, modulus = 73)
factorizepoly(f, 73)

