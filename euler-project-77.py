from prime_functions import *

N = 10
keepGoing = True
num = 0
while keepGoing:
    primes = getPrimes(N)
    l = len(primes)
    amounts = [[],[]] #the value of [m][n] gives the number of ways to sum to m only using primes as large as the nth prime
    for i in range(l):
        amounts[0].append(0)
        amounts[1].append(1)
    for n in range(2,N):
        amounts.append([])
        if n%2 == 1:
            amounts[n].append(1)
        else:
            amounts[n].append(0)
        for c in range(1,l):
            if n - primes[c] > 0:
                num = amounts[n][c-1]+amounts[n-primes[c]][c]
                amounts[n].append(num)
            else:
                amounts[n].append(amounts[n][c-1])
        if num > 50000:
            print(n-1)
            keepGoing = False
            break
    N*=10

print(n-1)