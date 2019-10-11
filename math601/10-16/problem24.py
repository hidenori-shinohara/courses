for n in range(8):
    found = False
    for x in range(8):
        for y in range(8):
            if (x * x - 2 * y * y - n) % 8 == 0:
                found = True
                print("(%d)^2 - 2(%d)^2 = %d" % (x, y, n))
                break
        if found: break
    if not found: print("No solution when n = %d" % n)



