from prime_functions import *
import itertools
import math
N = 1000000
primes = getPrimes(N)

print('done')
sum = 1 #including 2 despite the check below testing for even integers
index = 0
for x in primes:
    goodnumber = True
    l = len(str(x))
    for num in str(x): 
        if int(num)%2 == 0: #only need to test numbers if digits are all odd (apart from 2)
            goodnumber = False
    if not goodnumber:
        continue
    else:
        for i in range(l):
            numstring = ''
            for j in range(l):
                numstring += str(x)[(i+j)%l]
            if int(numstring) not in primes:
                goodnumber = False
        if goodnumber:
            sum += 1
print(sum)