
def isPrime(n):
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


for prime in range(2, 100):
    if isPrime(prime):
        for i in range(2, prime):
            if (i * i) % prime == 2:
                print("%d^2 = 2 (mod %d)" % (i, prime))
                break
