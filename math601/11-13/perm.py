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
    def cycle_notation(self):
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
        return hash((self.ls))



class TestPermutations(unittest.TestCase):
    def test_cycle_notation(self):
        p = Permutation([2, 1, 0, 4, 3])
        self.assertEqual(p.cycle_notation(), "(13)(45)")
        p = Permutation([2, 0, 1, 4, 3])
        self.assertEqual(p.cycle_notation(), "(132)(45)")
        p = Permutation(list(range(5)))
        self.assertEqual(p.cycle_notation(), "(1)")
    def test_multiply(self):
        p = Permutation([2, 1, 0, 4, 3])
        q = Permutation([0, 2, 1, 3, 4])
        self.assertEqual(p.multiply(q).cycle_notation(), "(132)(45)")
    def test_inverse(self):
        p = Permutation([1, 0, 2, 3, 4])
        self.assertEqual(p.inverse().cycle_notation(), p.cycle_notation())
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
    for p in H:
        if len(res) >= 2:
            res += ','
        res += p.cycle_notation()
    res += ']'
    print(res)
def remdup(ls):
    newls = []
    for i in range(len(ls)):
        seen = False
        for j in range(i):
            if ls[i] == ls[j]:
                seen = True
        if not seen:
            newls.append(ls[i])
    return newls

v = Permutation([1, 2, 0, 3])
H = [v]

def findclosure(ls):
    for i in range(24):
        newls = []
        for p in ls:
            newls.append(p)
            for q in ls:
                newls += [p.multiply(q)]
        newls = remdup(newls)
        print(len(ls))
        print(len(newls))
        if len(ls) == len(newls):
            print("HELLO")
            return newls
        ls = newls.copy()
print(printgroup(findclosure(H)))
