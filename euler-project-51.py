from prime_functions import *
import time
N = 1000000

primes = getPrimes(N)
end = False
m=0

for prime in primes:
    if prime < 100:
        continue
    l = len(str(prime))
    for i in str(prime):
        if str(prime).count(i) < 3:
            continue
        positions = []
        for j in range(l):
            if str(prime)[j] == i:
                positions.append(j)
        count = 0
        badcount = 0
        for k in range(10):
            numstring = ''
            for c in range(l):
                if c in positions:
                    numstring += str(k)
                else:
                    numstring += str(prime)[c]
            if int(numstring) in primes and numstring[0] != '0':
                count +=1
                if count == 8:
                    print(prime)
                    print(positions)
                    end = True
            
            else:
                badcount +=1
            
            if badcount == 3:
                break
        if end:
            break
    m += 1
    if m%10000==0:
        print(prime)
    if end:
        break