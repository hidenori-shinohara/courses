

ps = [2, 3, 5, 7, 11, 13, 17, 19]

for p in ps: 
    cnt = 0
    shouldPrint = False
    for a in range(p):
        for b in range(p):
            for c in range(p):
                for d in range(p):
                    if not (a * d - b * c) % p == 0:
                        cnt = cnt + 1
                        if shouldPrint and cnt <= 10:
                            print a, b
                            print c, d
                            print
                        
    print("prime = %d, cnt = %d" % (p, cnt))
    print("my formula = %d" % (p**4 - p**3 - p**2 + p))
