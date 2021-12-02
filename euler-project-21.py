totalsum = 0
for n in range(1,10000):
    sum = 0
    for i in range(1,n):
        if n%i == 0:
            sum += i
    sum2 = 0
    if sum != n:
        for i in range(1,sum):
            if sum%i == 0:
                sum2 += i
                
    if sum2 == n:
        print('Amicable pair found!')
        print(n)
        print(sum)
        totalsum += n
    if n%100 ==0:
        print(n)

print(totalsum)