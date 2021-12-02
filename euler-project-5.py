def lcm(x,num):
    max = 0
    for i in range(1,x+1):
        if num%i == 0 and x%i == 0:
            max = i
    return max

num = 1

for i in range(1,21):
    if num%(i) != 0:
        num *= int(i/lcm(i,num))
        print('num = ' + str(i))
        print(num)
        
print(num)

