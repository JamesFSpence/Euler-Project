sum = num = 0
for i in range(1,101):
    num += i**2
    sum += i
print(num)
print(sum)
print(num - sum**2)