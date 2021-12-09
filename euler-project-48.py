sum = 0
for x in range(1,11):
    pow = 1
    for j in range(x):
        pow *=x
        pow = pow%10000000000
    sum += pow
    sum = sum%10000000000
print(sum)