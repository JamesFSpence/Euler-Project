from prime_functions import *

def isPandigital(x):
    return len(set(str(x))) == len(str(x))

primes = sorted(getPrimes(18), reverse = True)
omegaset = [set(),set(),set(),set(),set(),set(),set()]
k=0
for prime in primes:
    i = 1
    if prime == 17:
        while prime*i < 1000:
            if isPandigital(prime*i):
                omegaset[0].add(str(prime*i).zfill(3))
            i+=1
    else:
        mults = set()
        while prime*i < 1000:
            numstring = str(prime*i).zfill(3)
            for item in omegaset[k-1]:
                if numstring[1::] == item[0:2] and isPandigital(numstring[0] + item):
                    omegaset[k].add(numstring[0]+item)
            i+=1
    k+=1


sum = 0
for num in omegaset[6]:
    for i in range(10):
        if isPandigital(str(i) + num):
            sum+= int(str(i)+ num)
            print(str(i) + num)
print(sum)