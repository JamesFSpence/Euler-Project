def isPalindromic(num):
    if str(num) == str(num)[::-1]:
        return True
    return False
import time
time.sleep(2)
count = 0

for i in range(10000):
    num = i
    p = False
    for step in range(50):
        numreverse = int(str(num)[::-1])
        num += numreverse
        if isPalindromic(num):
            p = True
            break
    if not p:
        count += 1

print(count)