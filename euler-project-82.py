with open("euler-project-82-text-file.txt") as f:
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
    bignum += matrix[0][i]

minpathmatrix = []
for i in range(N):
    minpathmatrix.append([])
    for j in range(N):
        minpathmatrix[i].append(bignum)

for j in range(N-1,-1,-1):
    change = True
    while change == True:
        change = False
        for i in range(N):
            if j == N-1:
                minpathmatrix[i][j] = matrix[i][j]
            else:
                if i == 0:
                    temp = minpathmatrix[i][j]
                    minpathmatrix[i][j] = matrix[i][j] + min(minpathmatrix[i+1][j],minpathmatrix[i][j+1])
                    if temp != minpathmatrix[i][j]:
                        change = True
                elif i == N-1:
                    temp = minpathmatrix[i][j]
                    minpathmatrix[i][j] = matrix[i][j] + min(minpathmatrix[i-1][j],minpathmatrix[i][j+1])
                    if temp != minpathmatrix[i][j]:
                        change = True
                else:
                    temp = minpathmatrix[i][j]
                    minpathmatrix[i][j] = matrix[i][j] + min(minpathmatrix[i-1][j],minpathmatrix[i+1][j],minpathmatrix[i][j+1])
                    if temp != minpathmatrix[i][j]:
                        change = True    

minimum = minpathmatrix[0][0]

for i in range(N):
    if minpathmatrix[i][0] < minimum:
        minimum = minpathmatrix[i][0]

print(minimum)