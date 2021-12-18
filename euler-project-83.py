with open("euler-project-83-text-file.txt") as f:
    m = f.read().splitlines()

matrix = []
for row in m:
    matrix.append(row.split(","))
m = None
bignum = 0
N = len(matrix)
for i in range(N):
    for j in range(N):
        matrix[i][j] = int(matrix[i][j])

bignum = 1000000
minpathmatrix = []
for i in range(N):
    minpathmatrix.append([])
    for j in range(N):
        minpathmatrix[i].append(bignum)
m=0
prevtotal = (N**2)*bignum
# for j in range(N-1,-1,-1):
change = True
while change == True:
    change = False
    for i in range(N):
        for k in range(N):
            if i == 0 and k == 0:
                minpathmatrix[i][k] = matrix[i][k]
            elif i == N-1 and k == 0:
                minpathmatrix[i][k] = matrix[i][k] + min(minpathmatrix[i-1][k],minpathmatrix[i][k+1])
            elif i == 0 and k == N-1:
                minpathmatrix[i][k] = matrix[i][k] + min(minpathmatrix[i+1][k],minpathmatrix[i][k-1])
            elif i == N-1 and k == N-1:
                minpathmatrix[i][k] = matrix[i][k] + min(minpathmatrix[i-1][k],minpathmatrix[i][k-1])
            elif i == N-1:
                minpathmatrix[i][k] = matrix[i][k] + min(minpathmatrix[i][k+1],minpathmatrix[i][k-1],minpathmatrix[i-1][k])
            elif i == 0:
                minpathmatrix[i][k] = matrix[i][k] + min(minpathmatrix[i][k+1],minpathmatrix[i][k-1],minpathmatrix[i+1][k])
            elif k == N-1:
                minpathmatrix[i][k] = matrix[i][k] + min(minpathmatrix[i+1][k],minpathmatrix[i][k-1],minpathmatrix[i-1][k])
            elif k == 0:
                minpathmatrix[i][k] = matrix[i][k] + min(minpathmatrix[i][k+1],minpathmatrix[i-1][k],minpathmatrix[i+1][k])
            else:
                minpathmatrix[i][k] = matrix[i][k] + min(minpathmatrix[i][k+1],minpathmatrix[i-1][k],minpathmatrix[i+1][k],minpathmatrix[i][k-1])
    total = 0
    for a in range(N):
        for b in range(N):
            total += minpathmatrix[a][b]
    if prevtotal > total:
        change = True
    prevtotal = total
print(minpathmatrix[N-1][N-1])