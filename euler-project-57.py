n = 1
d = 1
count = 0
for i in range(1000):
    n += 2*d
    d = n - d
    if len(str(n))>len(str(d)):
        count += 1
print(count)