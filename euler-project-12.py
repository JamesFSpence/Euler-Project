primes = []
n = 200000
for k in range(2,n+1):
    isPrime = True
    for i in primes:
        if i**2 > k:
            break
        elif k%i == 0:
            isPrime = False
            break
    if isPrime:
        primes.append(k)

keepGoing = True
ppowers = [{},{}]
x = 12300

while keepGoing:
    x+=1
    prod = 1
    ppowers.append({})
    ppowers.pop(0)
    for p in primes:
        if p>x:
            break
        if x%p == 0:
            index = 0
            y = x
            while y%p == 0:
                index +=1
                y = int(y/p)
            if p == 2:
                ppowers[1][str(p)] = index -1
            else:
                ppowers[1][str(p)] = index
    for p in ppowers[0]:
        if p in ppowers[1]:
            prod *= (ppowers[0][p] + ppowers[1][p] + 1)
        else:
            prod *= (ppowers[0][p] +1)
    for q in ppowers[1]:
        if q not in ppowers[0]:
            prod *= (ppowers[1][q] + 1)
    if prod > 500:
        keepGoing = False
    

print(ppowers)
print(x-1)
print(x)
print(((x*(x-1))/2))
