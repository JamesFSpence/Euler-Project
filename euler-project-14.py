x = 0
max = 0
known = {'1':0}
for i in range(1,1000000):
    n = i
    count = 0
    while str(n) not in known:
        if n%2 == 0:
            n = int(n/2)
        else:
            n = 3*n + 1
        count +=1
    known[str(i)] = known[str(n)] + count
    if known[str(i)] > max:
        max = known[str(i)]
        x = i

print(x)   