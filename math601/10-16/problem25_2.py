xs = [0, 1, 4]

for a in xs:
    for b in xs:
        print("%d - 2 \cdot %d \equiv %d" % (a, b, (a - 2 * b) % 8))
