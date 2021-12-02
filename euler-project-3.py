def findNextDivisible(x,divisible):
    for i in range(2,x):
        if x%i == 0:
            divisible.append(i)
            x = int(x/i)
            print(x)
            findNextDivisible(x,divisible)
    print(x)

findNextDivisible(600851475143,[])