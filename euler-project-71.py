import math

N = 1000000
mindiff = 1
for j in range(1,N):
    for i in range(math.ceil(j*(3/7 - mindiff)),j): #j>i as i/j < 1
        if 3/7 - i/j > 0 and 3/7 - i/j < mindiff:
            mindiff = 3/7 - i/j
            numerator = i
        elif 3/7 - i/j < 0:
            break

print(numerator)