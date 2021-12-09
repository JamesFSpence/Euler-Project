digits = {'1','2','3','4','5','6','7','8','9'}
max = 0
for x in range(100000):
    concat =str(x)
    k = 2
    keepGoing = True
    while keepGoing:
        concat += str(x*k)
        if len(concat)>9:
            keepGoing = False
        if set(concat) == digits and int(concat)>max and keepGoing:
            max = int(concat)
        
        k += 1

print(max)
