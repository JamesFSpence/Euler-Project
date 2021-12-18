keepGoing = True
n=0
mindiff = 2000000
for n in range(2001): #1 X 2000 reactangle has > 2000000 solutions
    n+=1
    for m in range(1,n+1):
        if abs((n*(n+1)/2)*(m*(m+1)/2) - 2000000)<mindiff:
            mindiff = abs((n*(n+1)/2)*(m*(m+1)/2) - 2000000)
            area = n*m

print(area)