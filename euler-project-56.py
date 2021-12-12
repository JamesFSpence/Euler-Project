maxsum = 0

for a in range(100):
    for b in range(100):
        sum = 0
        numstring = str(a**b)
        for char in numstring:
            sum += int(char)
        if sum > maxsum:
            maxsum = sum

print(maxsum)