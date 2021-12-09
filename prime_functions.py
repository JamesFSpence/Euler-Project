def getPrimes(n):
    primes = []
    for x in range(2,n+1):
        p = True
        for i in primes:
            if i**2 > x:
                break
            elif x%i == 0:
                p = False
                break
        if p:
            primes.append(x)
    return(primes)


def getPrimeDivisors(n,primes):
    primedivisors = []
    y = n
    for prime in primes:
        if prime > y:
            break
        index = 0
        while y%prime == 0:
            index+=1
            y=int(y/prime)
        if index > 0:
            primedivisors.append([prime,index])
    return primedivisors

def isPrime(n):
    i = 2
    while i**2 < n:
        if n%i ==0:
            return False
        i+=1
    return True