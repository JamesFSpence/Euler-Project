import time

time.sleep(2)
N = 10
i = 1

keepGoing = True
while keepGoing:
    while i < N/6:
        goodnumber = True
        i += 1
        ilist = sorted([char for char in str(i)])
        for j in range(1,6):
            numlist = sorted([char for char in str(i*(j+1))])
            if numlist != ilist:
                goodnumber = False
                break
        if goodnumber:
            print(i)
            keepGoing = False
            break
    i = N
    N*=10