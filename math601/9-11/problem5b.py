
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
def remdup(ls):
    res = []
    for i in range(len(ls)):
        if i > 0:
            if ls[i - 1] == ls[i]:
                continue
        res += [ls[i]]
    return res


                    
conjs = []
for m in ms:
    conj = []
    for n in ms:
        if not n == m:
            conj += [mul(mul(n, m), inv(n))]
    conj = remdup(sorted(conj))
    print conj
    conjs += [conj]

ls = remdup(sorted(conjs))
print "final"
cnt = 0
for l in ls:
    print l
    cnt += len(l)

print cnt

