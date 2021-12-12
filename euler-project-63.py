keepGoing = True
n = 1
while keepGoing:
    n+=1
    if len(str(9**n)) < n:
        N = n
        keepGoing = False

sum = 0

for k in range(1,N):
    for j in range(1,10):
        if j**k > 0 and len(str(j**k)) == k:
            sum += 1

print(sum)