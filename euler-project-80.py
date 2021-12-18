import math
N = 2 #number we are finding the square root of
k = 100 #number of decimal places
squares = [1,4,9,16,25,36,49,64,81]
sum = 0

for N in range(1,100):
    if N in squares:
        continue
    A = 0
    i = k
    while i > 0:
        i-=1
        while A**2 < N*10**(2*(k-1)):
            A += 10**i
        A -= 10**i

    for digit in str(A):
        sum += int(digit)

print(len(str(A)))
print(sum)