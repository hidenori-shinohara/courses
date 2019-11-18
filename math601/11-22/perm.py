from itertools import permutations
import unittest

class Permutation:
    def __init__(self, ls):
        self.ls = ls
        self.n = len(ls)
    def sends(self, i):
        return self.ls[i]
    def __eq__(self, other):
        for i in range(self.n):
            if self.sends(i) != other.sends(i):
                return False
        return True
    def __ne__(self, other):
        return not self.__eq__(other)
    def __lt__(self,other):
        return (str(self)<str(other))
    def __le__(self,other):
        return (str(self)<=str(other))
    def __gt__(self,other):
        return (str(self)>str(other))
    def __ge__(self,other):
        return (str(self)>=str(other))
    def __str__(self):
        seen = {}
        result = ""
        for i in range(self.n):
            if i not in seen:
                if i != 0 and self.ls[i] == i: continue
                result += "(" + str(i + 1)
                j = self.ls[i]
                while j != i:
                    seen[j] = True
                    result += str(j + 1)
                    j = self.ls[j]
                result += ")"
        if len(result) >= 4 and result[0:3] == "(1)":
            result = result[3:]
        return result
    def multiply(self, other):
        product = list(range(self.n))
        for i in range(self.n):
            product[i] = self.sends(other.sends(i))
        return Permutation(product)
    def inverse(self):
        inverse = list(range(self.n))
        for i in range(self.n):
            inverse[self.sends(i)] = i
        return Permutation(inverse)
    def __hash__(self):
        return hash('-'.join(str(i) for i in self.ls))

class TestPermutations(unittest.TestCase):
    def test_cycle_notation(self):
        p = Permutation([2, 1, 0, 4, 3])
        self.assertEqual(str(p), "(13)(45)")
        p = Permutation([2, 0, 1, 4, 3])
        self.assertEqual(str(p), "(132)(45)")
        p = Permutation(list(range(5)))
        self.assertEqual(str(p), "(1)")
    def test_multiply(self):
        p = Permutation([2, 1, 0, 4, 3])
        q = Permutation([0, 2, 1, 3, 4])
        self.assertEqual(str(p.multiply(q)), "(132)(45)")
    def test_inverse(self):
        p = Permutation([1, 0, 2, 3, 4])
        self.assertEqual(str(p.inverse()), str(p))
    def test_eq(self):
        p = Permutation([1, 0, 2, 3, 4])
        q = Permutation([1, 0, 2, 3, 4])
        self.assertEqual(p == q, True)
        p = Permutation([1, 0, 2, 3, 4])
        q = Permutation([0, 1, 2, 3, 4])
        self.assertEqual(p == q, False)

# unittest.main()

def printgroup(ls):
    res = '['
    for p in ls:
        if len(res) >= 2:
            res += ','
        res += str(p)
    res += ']'
    print(res)

v = Permutation([1, 2, 0, 3])
H = [v]

allperms = list(Permutation(p) for p in list(permutations([0, 1, 2, 3])))

def findclosure(ls):
    ls.append(Permutation([0, 1, 2, 3, 4]))
    for i in range(120):
        products = {Permutation([0, 1, 2, 3, 4])}
        for p in ls:
            for q in ls:
                products.add(p.multiply(q))
                if len(products) >= 61:
                    return sorted(allperms)
        if len(ls) == len(products):
            return sorted(products)
        ls = sorted(products)


def powperm(p, n):
    q = p
    for i in range(n - 1):
        q = q.multiply(p)
    return q

a = Permutation([1, 2, 3, 4, 0])
b = Permutation([0, 2, 4, 1, 3])
print(a)
print(b)

G = findclosure([a, b])
printgroup(G)
print(len(G))

anyRelation = False
for i in range(1, 5):
    for j in range(1, 4):
        if powperm(a, i) == powperm(b, j):
            anyRelation = True
if not anyRelation:
    print("No relation")
