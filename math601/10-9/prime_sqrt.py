
def isPrime(n):
    for d in range(2, n):
        if n % d == 0:
            return False
    return True


for prime in range(3, 18):
    if isPrime(prime):
        print("  \item (Modulo %d)" % prime)
        print("   ", end = " ")
        for i in range(2, prime):
            result = (i * i) % prime
            print("%d^2 \equiv %d," % (i, result), end = " ")
            if result == 2:
                break
        print("")
