import random

a = []
for i in range(10):
    n = a.append(int(random.random() * 100))
print(a)

even = 0
odd = 0
for i in a:
    if i%2 == 0:
        even += 1
    else:
        odd += 1
print("Even: ", even)
print("Odd: ", odd)
