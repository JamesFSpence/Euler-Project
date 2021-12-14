# To minimise n/phi(n) we need large primes dividing n.
# Strategy: to test primes near sqrt(10^7) and once we find a solution
# check all remaining possibilities using the fact that if p divides n,
# then n/phi(n) > p/(p-1).

# At any stage, we have a minimum for the ratio:
# n/phi(n), for n<N. Call it minrat
# and we only need to consider primes > minrat/(minrat - 1).

# Eg.87109/79180 = 1.1001...,
# 1.1/(1.1002 - 1) > 10
# so primes less than 10 cannot be included
# in the prime factorisation of n.
import math
from prime_functions import *

N = 10000000
minrat = 2
minprime = 1

K = math.ceil(1.5*math.sqrt(N))
primes = getPrimes(K) #we'll try with primes between 2000 and 5000
keepGoing = True
while keepGoing:
    i = 0
    for prime in primes:
        i+=1
        if prime < minprime:
            continue
        for prime2 in primes[i::]:
            prod = prime*prime2
            if prod > N:
                break
            totient = (prime-1)*(prime2-1)
            if sorted([char for char in str(prod)]) == sorted([char for char in str(totient)]) and prod/totient < minrat:
                minrat = prod/totient
                minprime = minrat/(minrat-1)
                number = prod
    if minprime < N/K:
        primes = getPrimes(math.ceil(N/minprime))
        K = N/minprime
    else:
        keepGoing = False

cr = (N)**(1/3)
if minrat > (cr/(cr-1))**3: #if this is true, there is a possibility the product of 3 primes produces a better ratio (it doesn't in the case of 10000000)
    print('oh no')

print(number)