def a(ls):
    res = [0] * 6
    res[2] = ls[1]
    res[3] = ls[2]
    res[4] = ls[3]
    res[5] = ls[4]
    res[1] = ls[5]
    return res
def b(ls):
    res = [0] * 6
    res[2] = ls[1]
    res[4] = ls[2]
    res[3] = ls[4]
    res[1] = ls[3]
    res[5] = ls[5]
    return res


def ab(m, n):
    ls = range(6)
    for i in range(n): ls = b(ls)
    for i in range(m): ls = a(ls)
    return ls

def ba(m, n):
    ls = range(6)
    for i in range(m): ls = a(ls)
    for i in range(n): ls = b(ls)
    return ls

for m in range(5):
    for n in range(4):
        p1 = ab(m, n)
        for l in range(5):
            for p in range(4):
                p2 = ba(l, p)
                if p1 == p2 and (m * n * l * p > 0):
                    print m, n, l, p


