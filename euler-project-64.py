import math
sum = 0
for i in range(1,10001):
    if math.sqrt(i).is_integer():
        continue
    n = (-1)*math.floor(math.sqrt(i))
    expansion = []
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
            if length%2 == 1:
                sum += 1
    print(expansion)
print(sum)