import math
total = 0

def coprime(p,q):
    if q>p:
        p = p+q
        q = p-q
        p = p-q
    while q != 0:
        qtemp = q
        q = p - math.floor(p/q)*q
        p = qtemp
        if p == 1:
            return True
    return False
import time
M=0
total = 0
primpairs = [set()] #primpairs[n] lists all the numbers x for which c = sqrt(x^2 + n^2) is an integer, and  x,n,c is a primitive

for i in range(2000): # from experimenting our solution is < 2000
    primpairs.append(set())

N = 2000
ceiling = math.ceil(math.sqrt((1+math.sqrt(5))*N)) # the highest value p can take and still satifsy the conditions
for p in range(1,ceiling): # every primitve pythagorean triple is off the form (p^2 - q^2, 2pq, p^2 + q^2), for p,q coprime with p != q (mod 2) and q < p.
    d = p%2 #iterate over odds if p is even and vice versa
    for q in range(d+1,p,2): #q<p
        if coprime(p,q):
            x = p**2 - q**2
            y = 2*p*q
            if x<=N and x: # we have x,y,z is a primitive pythagoren triple, and so every solution to a = x, b+c = y with a>=b>=c is a solution (shortest path is only a^2 + (b+c)^2 if b,c <= a)
                primpairs[x].add(y)
            if y <= N:
                primpairs[y].add(x)

while total < 1000000: #this is inefficient as we loop through the same values of p and q over anf over
    M+=1
    for num in primpairs[M]:
        total += max(min(M+1,num) - math.ceil(num/2),0) # adding up possibilities for primitve triples with M as the value of the longest edge of the cube
    for i in range(1,math.floor(M/2)+1):
        if M%i == 0:
            for num in primpairs[i]:
                bplusc = int(num*(M/i))
                total += max(min(M+1,bplusc) - math.ceil(bplusc/2),0) # adding up possibilities where M is a multiple of a num which is in a primitive triple
    if M%100 == 0:    
        print('For ' + str(M) + ': ' + str(total))

print(M)