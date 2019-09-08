
from sets import Set

ps = [3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41]

match = True
for p in ps: 
    cnt = 0
    shouldPrint = True
    for a in range(p):
        for b in range(p):
            for c in range(p):
                for d in range(p):
                    if (a * d - b * c) % p == 1:
                        cnt = cnt + 1
                        if shouldPrint and cnt <= 3:
                            print a, b
                            print c, d
                            print
                        
    print("prime = %d, cnt = %d" % (p, cnt))
    myanswer = p**3 - p
    match = match and (myanswer == cnt)
    print("my formula = %d" % myanswer)

if match:
    print("Congrats! All the numbers matched.")
else:
    print("Bummer! Some numbers didn't match.")


