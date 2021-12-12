expansion = []
N = 100 #number which you want to go to
k = 1
for i in range(N):
    if i == 0:
        expansion.append(2)
    elif i%3 == 2:
        expansion.append(2*k)
        k+=1
    else:
        expansion.append(1)

n = 1
d = expansion[N-1]
c = expansion[N-2]

for i in range(N-2):
    temp = n
    n = d
    d = c*d+temp
    c = expansion[N-3-i]

n += expansion[0]*d
# print(n/d)
# print(str(n) + '/' + str(d))

sum = 0
for char in str(n):
    sum += int(char)

print(sum)