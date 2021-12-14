import math
N = 12000
sum = 0
totient = [0,0]
primes = []
for i in range(2,N+1):
    totient.append(i)
print('done')
sum = 0

for i in range(2,math.ceil(N/2)): #we range over the possible numerators
    if i < int(N/3)+1: #if 3i < N then all q coprimes to i have a corprime to i given by q+2i, and q+2i will be less than N
        if totient[i] == i: #in this case i is prime, and we just add the totient of i
            primes.append(i)
            sum += i-1
            j = 2*i
            while j < N+1: #we alter the corresponding totients of all multiples of i
                totient[j]*=1-1/i
                j+=i
        else: # in this case i is composite and we've found the totient using previous primes
            sum += totient[i]
    else: #in this case only part of the range (2i,3i) is less than N
        if totient[i] == i: #if i is prime, count all numbers from 2i+1 to N (there are N-2i of them)
            primes.append(i)
            sum += N-2*i
            j = 2*i
            while j < N+1:
                totient[j]*=1-1/i
                j+=i
        else: #in this case we can find all primes dividing i and add all other products of that prime in (2i, 3i) to the set notcoprime
            notcoprimes = set()
            for prime in primes:
                if i%prime == 0:
                    y = 2*i+prime
                    while y < N+1: 
                        notcoprimes.add(y)
                        y+=prime
            sum+=N-2*i-len(notcoprimes) #the amount of numbers coprime is just the amount - the amount of notcoprime
    
print(sum)