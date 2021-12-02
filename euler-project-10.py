import math
primes = []
for x in range(2,2000000):
    isprime = True
    for i in primes:
        if x%i == 0:
            isprime = False
            break
        elif i > math.sqrt(x):
            break
    if isprime == True:
        primes.append(x)
    if x%10000 == 0:
        print(x)

sum = 0
for i in primes:
    sum += i

print(sum)
