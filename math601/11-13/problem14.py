ps = [3, 5, 7]

for p in ps:
    q = 1
    for e in range(3):
        q *= p # q = p ** e
        for k in range(q - 1):
            v = k * (q - 1) / 2 % (q - 1)
            print("%d(%d - 1)/2 = %d" % (k, q, v))




