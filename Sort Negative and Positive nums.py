import random

nums = []
for i in range(20):
    nums.append(int(random.random() * 20) - 10)
print(nums)

neg = []
pos = []
for i in nums:
    if i < 0:
        neg.append(i)
    else:
        pos.append(i)
print(neg)
print(pos)
