count = 0
keepGoing = True
denom = 11
num = 10
numprod = 1
denomprod = 1
while keepGoing:
    N = [char for char in str(num)]
    D = [char for char in str(denom)]
    if not (N[len(N)-1] == '0' and D[len(D)-1] == '0'):
        for i in range(len(N)):
            index = 0
            for j in range(D.count(N[i])):
                index = D.index(N[i],index)
                newN = []
                newD = []
                for k in range(len(N)):
                    if k != i:
                        newN.append(N[k])
                for j in range(len(D)):
                    if j != index:
                        newD.append(D[j])
                newNint = int("".join(newN))
                newDint = int("".join(newD))
                if denom*newNint == num*newDint:
                    count +=1
                    print(count)
                    print(str(num) + '/' + str(denom))
                    numprod*=num
                    denomprod*= denom
    if num+1<denom:
        num+=1
    else:
        denom+=1
        num = 10
    if count == 4:
        keepGoing = False

print(numprod)
print(denomprod)
