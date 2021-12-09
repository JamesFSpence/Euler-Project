N = 1001 #size of grid (only works for odd N)

total = 1
num = 1
diff = 0
M = int((N-1)/2)

for j in range(M):
    diff += 2
    for i in range(4):
        num+=diff
        total += num
print(total)
