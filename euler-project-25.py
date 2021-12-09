a = 1
b = 1
keepGoing = True
count = 2
while keepGoing:
    b = a+b
    a = b-a
    count += 1
    if len(str(b)) == 1000:
        print(b)
        print(count)
        keepGoing = False
    