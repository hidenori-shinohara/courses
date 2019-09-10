conjugacy_classes = [[[[0, 1], [2, 0]], [[0, 2], [1, 0]], [[1, 1], [1, 2]], [[1, 2], [2, 2]], [[2, 1], [1, 1]], [[2, 2], [2, 1]]], [[[0, 1], [2, 1]], [[1, 1], [2, 0]], [[2, 0], [2, 2]], [[2, 1], [0, 2]]], [[[0, 1], [2, 2]], [[1, 0], [2, 1]], [[1, 1], [0, 1]], [[2, 1], [2, 0]]], [[[0, 2], [1, 1]], [[1, 2], [1, 0]], [[2, 0], [1, 2]], [[2, 2], [0, 2]]], [[[0, 2], [1, 2]], [[1, 0], [1, 1]], [[1, 2], [0, 1]], [[2, 2], [1, 0]]], [[[1, 0], [0, 1]]], [[[2, 0], [0, 2]]]]

from sets import Set

p = 3

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

def mul(m, v):
    return [m[0][0] * v[0] + m[0][1] * v[1], m[1][0] * v[0] + m[1][1] * v[1]]

def eq(v1, v2):
    return (v1[0] - v2[0]) % p == 0 and (v1[1] - v2[1]) % p == 0

def printmat(m):
    print("\\begin{bmatrix} %d & %d \\\\ %d & %d \\end{bmatrix}," % (m[0][0], m[0][1], m[1][0], m[1][1]))
                    
for conj_class in conjugacy_classes:
    for a in range(p):
        for b in range(p):
            if a == 0 and b == 0: continue
            for m in conj_class:
                is_eigen_vector = eq(mul(m, [a, b]), [a, b])
                is_eigen_vector |= eq(mul(m, [a, b]), [2 * a, 2 * b])
                if is_eigen_vector:
                    print "&"
                    printmat(m)
                    print
                    break
    print "============="

for a in range(p):
    for b in range(p):
        print("\\begin{bmatrix} %d \\\\ %d \\end{bmatrix}," % (a, b))
