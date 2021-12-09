import math

keepGoing = True
def isPentagonal(int):
    f = (1 + math.sqrt(1+24*int))/6
    return f.is_integer()


pentagonal = [1]

i = 0
while keepGoing:
    i+=1
    pentagonal.append(int(i*(3*i-1)/2))
    p = pentagonal[i]
    for j in range(i):
        q = pentagonal[j]
        if isPentagonal(p-q) and isPentagonal(p+q):
            print(p-q)
            print(p)
            print(q)
            keepGoing = False