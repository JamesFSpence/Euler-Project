from prime_functions import *
M = 100000
smallPrimes = getPrimes(1000)
primes = getPrimes(M)
max = 0

for b in smallPrimes:
    for a in range(-b,1000):
        count = 0
        keepGoing = True
        n = 0
        while keepGoing:
            output = n**2 + a*n + b
            if output > M:
                primes = primes + getPrimes(output, M)
                M = output
            if output in primes:
                count+=1
            else:
                keepGoing = False       
            n+=1
        if count>max:
            max = count
            maxprod = a*b
print(maxprod)