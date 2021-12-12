#~2 mins runtime

from prime_functions import *

n = 1
k = 0
totalp = 0
keepGoing = True
while keepGoing:
    k+=2
    for i in range(3):
        n+=k
        if isPrime(n):
            totalp +=1
    n+=k
    if totalp/(2*k + 1) < 0.1:
        keepGoing = False
print('Answer:')
print(k+1)