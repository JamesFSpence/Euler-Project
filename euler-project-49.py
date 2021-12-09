from prime_functions import *
import math

primes = getPrimes(9986)

digits = ['','','']
end = False
numstring = ''
for prime in primes:
    if prime < 1000 or prime == 1487:
        continue
    for j in range(6,int(math.floor(10000-prime)/2),6):
        if (prime + j) in primes and (prime + j + j) in primes:
            digits[0] = sorted(list(str(prime)))
            digits[1] = sorted(list(str(prime+j)))
            digits[2] = sorted(list(str(prime+j+j)))
            if digits[0] == digits[1] and digits[0] == digits[2]:
                numstring = str(prime) + str(prime + j) + str(prime + j + j)
                end = True
    if end:
        break
    

print(numstring)