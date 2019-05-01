numsOrigin = [-24, 3, 45, 31, 0, -14, 0, -15, -1, 7]
numsReplaced = []
for i in numsOrigin:
    if i < 0:
        numsReplaced.append(-1)
    elif i > 0:
        numsReplaced.append(1)
    else:
        numsReplaced.append(i)
print(numsOrigin)
print(numsReplaced)
