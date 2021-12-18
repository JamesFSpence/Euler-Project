with open("euler-project-81-text-file.txt") as f:
    m = f.read().splitlines()

matrix = []
for row in m:
    matrix.append(row.split(","))
    
N = len(matrix)
minpathmatrix = []
for i in range(N):
    minpathmatrix.append([])
    for j in range(N):
        minpathmatrix[i].append(0)

for i in range(N):
    for j in range(N):
        matrix[i][j] = int(matrix[i][j])

for k in range(2*(N - 1),-1,-1):
    for j in range(max(0,k-N+1),min(k+1,N)):
        i = k - j
        if i == N-1:
            if j == N-1:
                minpathmatrix[i][j] = matrix[i][j]
            else:
                minpathmatrix[i][j] = matrix[i][j] + minpathmatrix[i][j+1]
        elif j == N-1:
            minpathmatrix[i][j] = matrix[i][j] + minpathmatrix[i+1][j]
        else:
            minpathmatrix[i][j] = matrix[i][j] + min(minpathmatrix[i+1][j],minpathmatrix[i][j+1])

print(minpathmatrix[0][0])
