import math
maxD = 1
max_x = 1

def findFraction(N,expansion,length): #funciton to find the fraction obtained from taking the first N numbers of the infinite fraction expansion
    while len(expansion) < N:
        l = len(expansion)
        for j in range(length):
            expansion.append(expansion[l-length+j])
    numer = 1
    denom = expansion[N-1]
    const = expansion[N-2]
    for i in range(N-2):
        temp = numer
        numer = denom
        denom = const*denom+temp
        const = expansion[N-3-i]
    numer += expansion[0]*denom
    return[numer,denom]

for i in range(1,1001):
    if math.sqrt(i).is_integer(): #i is square we skip
        continue
    n = (-1)*math.floor(math.sqrt(i)) #the following is the method to find the infinite fraction expansion of sqrt(i)
    expansion = [-n]
    d = 1
    appeared = []
    keepGoing = True
    while keepGoing:
        appeared.append([n,d])
        d = int((i - n**2)/d)
        expansion.append(math.floor((math.sqrt(i)-n)/d))
        n = - n - d*math.floor((math.sqrt(i)-n)/d)
        if [n,d] in appeared:
            length = len(appeared) - appeared.index([n,d])
            keepGoing = False
    N = 0
    keepGoing = True
    while keepGoing: #iteratively expanding the infinite fraction until a solution is found (solutions must be obtained from the fractional expansion)
        N+=1
        frac = findFraction(N,expansion,length)
        if frac[0]**2 - i*(frac[1]**2) == 1:
            print(frac[0])
            keepGoing = False
            if frac[0] > max_x:
                max_x = frac[0]
                maxD = i
                
print(maxD)
print(max_x)