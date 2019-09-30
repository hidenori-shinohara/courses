from itertools import permutations
import unittest

class Permutation:
    def __init__(self, ls):
        self.ls = ls
        self.n = len(ls)
    def sends(self, i):
        return self.ls[i]
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

# unittest.main()

all_permutations = list(permutations(list(range(3))))

list_a = [[0, 1, 2], [1, 0, 2], [1, 0, 2], [1, 0, 2], [0, 1, 2], [1, 2, 0], [0, 2, 1], [1, 2, 0]]
list_b = [[0, 1, 2], [0, 1, 2], [2, 1, 0], [1, 2, 0], [1, 2, 0], [2, 0, 1], [0, 2, 1], [1, 2, 0]]

cnt = 0
casenumber = 0
print("  \\begin{itemize}")
for i in range(len(list_a)):
    for j in range(2):
        a = Permutation(list_a[i])
        b = Permutation(list_b[i])
        if j == 1:
            if i in [0, 2, 5, 6, 7]:
                continue
            else:
                a, b = b, a
        casenumber += 1
        print("    \\item Case %d: $\\phi_{%d}: a \mapsto %s, b \mapsto %s$" % (casenumber, casenumber, a.cycle_notation(), b.cycle_notation()))
        conjugations = set()
        for p in all_permutations:
            perm = Permutation(p)
            conja = perm.inverse().multiply(a).multiply(perm).cycle_notation()
            conjb = perm.inverse().multiply(b).multiply(perm).cycle_notation()
            conjugations.add("$a \mapsto %s, b \mapsto %s$" % (conja, conjb))

        print("      The following maps are conjugates of $\phi_{%d}$" % (casenumber))
        print("      \\begin{itemize}")
        for conjugation in conjugations:
            print("        \\item " + conjugation)
            cnt += 1
        print("      \\end{itemize}")
print("  \\end{itemize}")
