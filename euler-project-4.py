def IsPalindrome(x):
    xString = str(x)
    for i in range(len(xString)):
        if xString[i] != xString[len(xString)-i-1]:
            return False
    return True

max = 0
for i in range(100,1000):
    for j in range(100,1000):
        if IsPalindrome(i*j) and i*j > max:
            max = i*j

print(max)