import math
def isPalindrome(str):
    l = len(str)
    for i in range(int(math.floor(l/2))):
        if str[i] != str[l-1-i]:
            return False
    return True

N = 1000000
sum = 0
for x in range(N):
    if isPalindrome(str(x)) and isPalindrome("{0:b}".format(x)):
        sum += x

print(sum)