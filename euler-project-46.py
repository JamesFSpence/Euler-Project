from prime_functions import *
import math

N = 10000

primes = getPrimes(N)
primes.pop(2)
squares = set()
for j in range(math.floor(math.sqrt(N))):
    squares.add(j**2)

i = 1
goodnumber = False
keepGoing = True
while keepGoing:
    i+= 2
    if i in primes:
        continue
    else:
        goodnumber = False
        for prime in primes:
            if prime > i:
                break
            elif int((i - prime)/2) in squares:
                goodnumber = True
        if goodnumber == False:
            print(i)
            keepGoing = False