import math

def isPentagonal(int):
    f = (1+math.sqrt(1+24*int))/6
    return f.is_integer()
def isTriangular(int):
    f = (-1+math.sqrt(1+8*int))/2
    return f.is_integer()


n = 143

keepGoing = True

while keepGoing:
    n+=1
    h = n*(2*n-1)
    if isPentagonal(h) and isTriangular(h):
        keepGoing = False
        print(h)
        print(n)

