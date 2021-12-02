count = 0
primes = []
x = 1
while count < 10001:
    x += 1
    isprime = True
    for i in primes:
        if x%i == 0:
            isprime = False
            break
    if isprime == True:
        primes.append(x)
        count += 1
        if count%100 == 0:
            print(count)
print(x)