n = 2**1000
sum = 0
for i in range(len(str(n))):
    sum += int(str(n)[i])
print(sum)