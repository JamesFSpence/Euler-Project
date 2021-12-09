import itertools
import math

def isPrime(x):
    for i in range(2,int(math.floor(math.sqrt(x)))):
        if x%i ==0:
            return False
    return True

m = ''
for x in range(4,10):
    r = []
    for i in range(1,x+1):
        r.append(str(i))
    perms = itertools.permutations(r)
    for perm in perms:
        if isPrime(int(''.join(perm))):
            m = ''.join(perm)

    print(x)

print(m)
