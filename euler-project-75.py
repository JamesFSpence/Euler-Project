import math

N = 1500000
amounts = []
for i in range(N+1): # array of N+1 zeros, where eventually the value in index i represents the number of triples totalling to i.
    amounts.append(0)

def coprime(p,q):
    if q>p:
        p = p+q
        q = p-q
        p = p-q
    while q != 0:
        qtemp = q
        q = p - math.floor(p/q)*q
        p = qtemp
        # print(str(p) + ' and ' + str(q))
        if p == 1:
            return True
    return False

for p in range(1,math.ceil(math.sqrt(N/2))): # every primitve pythagorean triple is off the form (p^2 - q^2, 2pq, p^2 + q^2), for p,q coprime with p != q (mod 2) and q < p.
    a = p%2 #iterate over odds if p i even and vice versa
    for q in range(a+1,min(p,math.ceil(N/(2*p) - p)),2): #q<p, and the sum of sides is 2p(p+q), which we want < N.
        if coprime(p,q):
            length = 2*p*(p+q)
            j = 1
            while length*j <= N: # once a primitve triple is found, we count all multiples of the triple up to N.
                amounts[length*j] += 1
                j+=1
            # print(str(p**2 - q**2) + ', ' + str(2*p*q) + ', ' + str(p**2 + q**2))

total = 0
for i in range(N+1):
    if amounts[i] == 1:
        total += 1

print(total)
#print(amounts)