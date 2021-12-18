import math

# n = 0
# keepGoing = True
# total = 1
# while keepGoing:
#     n+=1
#     amounts.append([1])
#     for k in range(1,n):
#         if k+1>n/2:    
#             amounts[n].append(amounts[n-1][k-1])
#         else:
#             amounts[n].append((amounts[n-1][k-1] + amounts[n-k-1][k])%1000000)
#     for k in range(0,math.ceil((n+1)/2)-1):
#         total += amounts[n-k-1][k]
#     total = total%1000000
#     if total%1000000 == 0:
#         print(n)
#         keepGoing = False
#     if n%1000 == 0:
#         print(n)
#         print(amounts[n][math.floor(n/2):math.floor(n/2)+10])
    
genpent = []
i = 1


    
coeffs = [1,1,-1,-1]
amounts = [1] #amounts[n] is the no of ways to partition n
keepGoing = True
n = 0

N = 1000000
while i*(3*i-1)/2 < N: #recursive formula for amounts[n] is given by alternatively summing previous values given by these "generalised pentagonal numbers"
    genpent.append(int(i*(3*i-1)/2))
    genpent.append(int(i*(3*i+1)/2))
    i+=1

while keepGoing:
    n+=1
    i = 0
    sum = 0
    while genpent[i]<=n:
        coeff = coeffs[i%4]
        sum += coeff*amounts[n-genpent[i]]
        i+=1
    if sum%N == 0:
        print(n)
        keepGoing = False
    amounts.append(sum)
