import math
from prime_functions import *

N = 50000000
maxc = math.floor(N**(1/4))
maxb = math.floor(N**(1/3))
maxa = math.floor(N**(1/2))

aprimes = getPrimes(maxa)
bprimes = getPrimes(maxb)
cprimes = getPrimes(maxc)

counted = set()
for a in aprimes:
    for b in bprimes:
        for c in cprimes:
            num = a**2 + b**3 + c**4
            if num >= N:
                break
            else:
                counted.add(num)

print(len(counted))