from prime_functions import *

N = 1000000

if N<2:
    print('please set N greater than 2')

primes = getPrimes(N)

print('done')
i = 0
maxj = 1
maxprime = 2

for prime in primes:
    if prime>N/maxj:
        break
    j = 0
    sum = 0
    for k in range(maxj+1):
        sum+=primes[i+k]
    j = maxj
    while True:  
        j+=1
        sum+=primes[i+j]
        if sum > N:
            break
        elif sum in primes:
            maxj = j+1
            maxprime = sum
    print(prime)
    i+=1

print(maxj)
print(maxprime)