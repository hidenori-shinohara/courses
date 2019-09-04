
from sets import Set

ps = [5]

# for p in ps: 
#     cnt = 0
#     shouldPrint = False
#     for a in range(p):
#         for b in range(p):
#             for c in range(p):
#                 for d in range(p):
#                     if not (a * d - b * c) % p == 0:
#                         cnt = cnt + 1
#                         if shouldPrint and cnt <= 10:
#                             print a, b
#                             print c, d
#                             print
#                         
#     print("prime = %d, cnt = %d" % (p, cnt))
#     print("my formula = %d" % (p**4 - p**3 - p**2 + p))

for p in ps: 
    print("prime = %d", p)
    for e in range(p):
        for f in range(p):
            ls = []
            for a in range(p):
                for b in range(p):
                    for c in range(p):
                        for d in range(p):
                            if not (a * d - b * c) % p == 0:
                                ls += [((a * e + b * f) % p, (c * e + d * f) % p)]
#                                print ("(%d, %d)" % ((a * e + b * f) % p, (c * e + d * f) % p))
            print Set(sorted(ls))
