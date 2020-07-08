import math as m
n = int(input("Enter a number: "))


def count(n):
    return n < 10 and 1 or 1 + count(n/10)


def isArmstrong(n):
    temp = n
    sum = 0
    count = 0
    while n > 0:
        count += 1
        n//=10
    n = temp
    while n>0:
        sum += (n%10)**count
        n//=10
    return sum == temp

if isArmstrong(n):
    print("YES")
else:
    print("NO")