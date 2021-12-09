total = 0

for x in range(10,413343): #9^5 *7 has seven digits -> only need to take x up to 9^5 *6 = 413343
    sum = 0
    digits = [int(i) for i in str(x)]
    for j in digits:
        sum += j**5
    if sum == x:
        total += x
        print(x)
print(total)