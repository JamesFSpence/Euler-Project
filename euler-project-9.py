for i in range(1,1001):
    for j in range(1, 1001-i):
        numbers = [str(i), str(j), str(1000-i-j)]
        if i**2 + j**2 + (1000-i-j)**2 == 2*int(max(numbers))**2:
            print(i*j*(1000-i-j))
            print(numbers)
