import math
keepGoing = True
N = 1
possible = []
while keepGoing:
    N*=10**(1/3)
    cubesdigits = dict()
    for i in range(math.floor(N),math.ceil(N*10**(1/3))):
        sortedchars = ''.join(sorted([char for char in str(i**3)]))
        #if sortedchars == '012334556789':
            #print(i)
        if sortedchars in cubesdigits:
            cubesdigits[sortedchars] += 1
            if cubesdigits[sortedchars] == 5:
                possible.append(sortedchars)
            if cubesdigits[sortedchars] == 6:
                possible.remove(sortedchars)
        else:
            cubesdigits[sortedchars] = 1
    if possible != []:
        break

for i in range(math.floor(N),math.ceil(N*10**(1/3))):
    sortedchars = ''.join(sorted([char for char in str(i**3)]))
    if sortedchars in possible:
        print(i**3)
        break