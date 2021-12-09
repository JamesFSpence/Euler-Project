import math

def nCr(n,r):
    return int(math.factorial(n)/(math.factorial(r)*math.factorial(n-r)))

count = 0
for n in range(23,101):
    for r in range(math.floor(n/2)+1): #nCr is symmetric so only need to test half of the r's
        if nCr(n,r) > 1000000: #nCr is increasing up to halfway so can assume > 1000000 for some r's 
            count += n + 1 - r*2
            break

print(count)