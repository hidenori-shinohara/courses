
from sets import Set

p = 3

def mul(m1, m2):
    m = [[0, 0], [0, 0]]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                m[i][j] = (m[i][j] + m1[i][k] * m2[k][j]) % p
    return m

def det(m):
    return m[0][0] * m[1][1] - m[0][1] * m[1][0]

def inv(m):
    a, b, c, d = m[0][0], m[0][1], m[1][0], m[1][1]
    v = det(m)
    return [[v * d, v * -b], [v * -c, v * a]]

ms = []
for a in range(p):
    for b in range(p):
        for c in range(p):
            for d in range(p):
                if (a * d - b * c) % p == 1:
                    ms += [[[a, b], [c, d]]]
def remove_duplicates(ls):
    res = []
    for i in range(len(ls)):
        if i > 0:
            if ls[i - 1] == ls[i]:
                continue
        res += [ls[i]]
    return res

def printmat(m):
    print("\\begin{bmatrix} %d & %d \\\\ %d & %d \\end{bmatrix}," % (m[0][0], m[0][1], m[1][0], m[1][1]))
                    
conjs = []
for m in ms:
    conj = []
    for n in ms:
        if not n == m:
            conj += [mul(mul(n, m), inv(n))]
    conj = remove_duplicates(sorted(conj))
    conjs += [conj]

ls = remove_duplicates(sorted(conjs))

for l in ls:
    for m in l:
        printmat(m)
    print

print ls
