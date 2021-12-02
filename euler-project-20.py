import math 

s = math.factorial(100)
sum = 0
for i in range(len(str(s))):
    sum += int(str(s)[i])
print(sum)