import math

def digitfact(n):
    sum = 0
    for char in str(n):
        sum += math.factorial(int(char))
    return sum

masterset = [2]
N = 1000000

for i in range(1,2177281):
    masterset.append(-1)

total = 0
maxchain = 1
for i in range(1,N):
    if masterset[i] == -1:
        seen = [i]
        keepGoing = True
        n = i
        diff = 0
        while True:
            diff += 1
            n = digitfact(n)
            if masterset[n] != -1:
                k = masterset[n]
                for j in range(diff):
                    masterset[seen[j]] = k + diff - j
                break
            if n in seen:
                keepGoing = False
                l = seen.index(n)
                for m in range(diff):
                    masterset[seen[m]] = max(diff-m,diff-l)
                break
            seen.append(n)
    if i%100000==0:
        print(i)
    if masterset[i] == 60:
        total +=1
    if masterset[i] > maxchain:
        maxchain = masterset[i]

print(total)   