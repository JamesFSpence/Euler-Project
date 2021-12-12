from prime_functions import *

smallprimes = getPrimes(10000)
print('done')

def getPossiblePrimes(p,smallprimes):
    possibleprimes = set()
    if p == 2:
        return possibleprimes
    lenp = len(str(p))
    for q in smallprimes:
        if q <= p:
            continue
        if isPrime(int(str(q) + str(p))) and isPrime(int(str(p)+str(q))):
            possibleprimes.add(q)
    return possibleprimes
found = False
poss = ['','','','']
chosenprimes = []
for p in smallprimes:
    chosenprimes = [p]
    poss[0] = getPossiblePrimes(p,smallprimes)
    if len(poss[0])>3:
        for q in poss[0]:
            chosenprimes.append(q)
            poss[1] = getPossiblePrimes(q,poss[0])
            if len(poss[1])>2:
                for r in poss[1]:
                    chosenprimes.append(r)
                    poss[2] = getPossiblePrimes(r,poss[1])
                    if len(poss[2])>1:
                        for s in poss[2]:
                            chosenprimes.append(s)
                            poss[3] = getPossiblePrimes(s,poss[2])
                            if len(poss[3])>0:
                                print(chosenprimes)
                                print(poss[3])
                                found  = True
                            chosenprimes.remove(s)
                    chosenprimes.remove(r)
            chosenprimes.remove(q)
    if found:
        break
