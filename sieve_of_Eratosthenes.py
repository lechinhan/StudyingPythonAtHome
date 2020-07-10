#Generate a prime list with sieve of Eratosthenes Algorithm

import math


def sieve_of_Eratosthenes(limit):
    temp_sieve = [True] * (limit+1)
    p = 2
    # 0 and 1 is not a prime number
    temp_sieve[0] = temp_sieve[1] = False
    while p * p <= limit:
        if temp_sieve[p]:
            for index in range(p * p, limit + 1, p):
                temp_sieve[index] = False
        p += 1
    primes = []
    #Generate a prime list
    for index in range(2, limit+1):
        if temp_sieve[index]:
            primes.append(index)
    return primes


print(sieve_of_Eratosthenes(10000000))