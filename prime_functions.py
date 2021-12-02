def getPrimes(n):
    primes = []
    for x in range(2,n+1):
        isPrime = True
        for i in primes:
            if i**2 > x:
                break
            elif x%i == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(x)
    return(primes)

def getPrimeDivisors(n,primes):
    primedivisors = dict()
    for prime in primes:
        index = 0
        y = prime
        while n%y == 0:
            index+=1
            y*=prime
        if index >0:
            primedivisors[prime] = index
    return primedivisors

primes = getPrimes(28123)

print('done!')
for n in range(1,28123):
    print(getPrimeDivisors(n,primes))