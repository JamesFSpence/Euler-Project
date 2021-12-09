total = 0
used = []
for num1 in range(100):
    for num2 in range(num1,10000):
        num3 = num1*num2
        numstring = str(num1) + str(num2) + str(num3)
        if len(numstring) == 9 and len(set(numstring)) == 9 and '0' not in set(numstring):
            if num3 not in used:
                used.append(num3)
                total += num3
                print(used)

print(total)
        
