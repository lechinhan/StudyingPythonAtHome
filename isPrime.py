import math as m


def isPrime(n):
    if n == 2:
        return 1
    if n == 1 or n % 2 == 0:
        return 0
    for i in range(3, int(m.sqrt(n) + 1)):
        if n % i == 0:
            return 0
    return 1


n = int(input())
if isPrime(n):
    print(n, "is a prime number")
else:
    print(n, "is not a prime number")
