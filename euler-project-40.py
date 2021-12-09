keepGoing = True
x = 0
digitcount = 0
prod = 1
count = 0
chosennumbers = {1,10,100,1000,10000,100000,1000000}
while keepGoing:
    x+=1
    for j in range(len(str(x))):
        digitcount +=1
        if digitcount in chosennumbers:
            prod*=int(str(x)[j])
            count += 1
    if digitcount>max(chosennumbers):
        keepGoing = False
print(prod)


