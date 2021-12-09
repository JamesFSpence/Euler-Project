from prime_functions import *

N = 10000 #even though the output > 10000, it still works

primes = getPrimes(N)
print('done')
i = 0
k = 4 #length of sequence we are looking for
keepGoing = True
while keepGoing:
    i+=1
    count = 0
    for j in range(k):
        if len(getPrimeDivisors(i + (k - 1) - j,primes)) != k:
            i+=k-1-j
            continue
        else:
            count += 1
    if count == k:
        print(i)
        keepGoing = False
    if i%1000 == 0:
        print(i)