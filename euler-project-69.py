def findNextPrime(n):
    i = 0
    while True:
        prime = True
        i+=1    
        for k in range(2,n+i):
            if (n+i)%k == 0:
                prime = False
                break
        if prime:
            return n+i

p = 2
prod = 2
tot = 1
while True:
    p = findNextPrime(p)
    if prod*p > 1000000:
        break
    prod *=p
    tot *= p-1

print(prod)