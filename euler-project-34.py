fact = {0:1,1:1,2:2,3:6,4:24,5:120,6:720,7:5040}
for i in range (10):
    factorial = 1
    if i ==0:
        fact[i] = 1
    else:
        for j in range(1,i+1):
            factorial *= j
        fact[i] = factorial

total = 0
for x in range(3,2178000):
    sum = 0
    for char in str(x):
        sum+= fact[int(char)]
    if sum == x:
        total += x

print(total)