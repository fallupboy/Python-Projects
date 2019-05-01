a = int(input("Type the first number: "))
b = int(input("Type the second number: "))
while a != 0 and b != 0:
    if a > b:
        a = a % b
    else:
        b = b % a
gcd = a + b
print(gcd)