#Find Greatest Common Divisor and Least Commom Multiple of 2 integer

#Euclidean Algorithm
def GCD(a, b):
    return a if b == 0 else GCD(b, a % b)
#Or you can simply use math.gcd (xD)

def LCM(a, b):
    return a*b // GCD(a, b)

while True:
    try:
        a = int(input("Enter value of a: "))
        b = int(input("Enter value of b: "))
        break
    except:
        print("Invalid input, enter again!")

a = abs(a)
b = abs(b)
print(f"GCD = {GCD(a, b)}")
print(f"LCM = {LCM(a, b)}")