import math
import numpy as np

M = 200 #total you want to find
coins = [1,2,5,10,20,50,100,200] #coins being used
l = len(coins)

matrix = np.ones((M+1,l))

for i in range(M+1):
    for j in range(1,l):
        if coins[j]<=i:
            matrix[i][j] = matrix[i][j-1] + matrix[i-coins[j]][j]
        else:
            matrix[i][j] = matrix[i][j-1]

print(matrix[200][7])