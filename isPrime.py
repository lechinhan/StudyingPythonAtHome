import math


def isPrime(n):
    if n == 2 or n == 3:
        return True
    if n < 2 or n % 2 == 0 or n % 3 == 0:
        return False
    lim = math.floor(math.sqrt(n))
    for item in range(3, lim + 1, 6):
        if n % item == 0 or n % (item+2) == 0:
            return False
    return True


n = int(input())
if isPrime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
