import math
import numpy as np

abundant = []
for x in range(1,28123):
    if x%1000==0:
        print(x)
    if x not in abundant:
        sum = 0
        for i in range(1,x):
            if x%i == 0:
                sum+=i
        if sum > x:
            abundant.append(x)
            y = math.floor(np.log2(28123/x))
            for i in range(1,y+1):
                abundant.append(x*2**i)

print(len(abundant))

# sumofabundant = []
# for num in abundant:
#     for mun in abundant:
#         if num+mun>28123:
#             break
#         else:
#             sumofabundant.append()


# #for i in range(28123):
