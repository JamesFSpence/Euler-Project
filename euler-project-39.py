import math

m = 0
pmax = 0
squares = []
for i in range(1000):
    squares.append(i**2)

count = []
for j in range(1001):
    count.append(0)

for a in range(1,333):
    for b in range(a,500):
        csquared = a**2 + b**2
        if csquared in squares:
            c = int(math.sqrt(csquared))
            if a+b+c <1001:
                count[a+b+c] += 1

print(count.index(max(count)))

