from prime_functions import *
N = 1000000

primes = getPrimes(N)
count = 0
total = 0

for prime in primes:
    goodnumber = True
    if len(str(prime)) == 1:
        continue
    if int(str(prime)[:-1]) in primes and int(str(prime)[1::]) in primes:
        for i in range(1,len(str(prime))):
            if not (int(str(prime)[:-i]) in primes and int(str(prime)[i::]) in primes):
                goodnumber = False
        if goodnumber:
            total += prime
            count += 1
            print(count)
            print(prime)
                

print(total)