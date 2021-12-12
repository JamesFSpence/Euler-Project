import math
import itertools
import time


nums = [[],[],[],[],[],[]]
n = 0

keepGoing = True
while keepGoing:
    n+=1
    if n*(n+1)/2 > 10000:
        break
    elif n*(3*n-2) < 1000:
        continue
    for i in range(3,9):
        num = int(n*(n*((i-2)/2) - (i-4)/2))
        if num < 1000 or num > 10000:
            continue
        else:
            if str(num)[0] != '0' and str(num)[2] != '0':
                nums[i-3].append(num)

time.sleep(2)
ends = ['','','','','']
perms = itertools.permutations(range(5))
escape = False
for perm in perms:
    if escape:
        break
    for num1 in nums[5]:
        if escape:
            break
        ends[0] = str(num1)[2:4]
        for num2 in nums[perm[0]]:
            if escape:
                break
            if ends[0] == str(num2)[0:2]:
                ends[1] = str(num2)[2:4]
                for num3 in nums[perm[1]]:
                    if escape:
                        break
                    if ends[1] == str(num3)[0:2]:
                        ends[2] = str(num3)[2:4]
                        for num4 in nums[perm[2]]:
                            if escape:
                                break
                            if ends[2] == str(num4)[0:2]:
                                ends[3] = str(num4)[2:4]
                                for num5 in nums[perm[3]]:
                                    if escape:
                                        break
                                    if ends[3] == str(num5)[0:2]:
                                        ends[4] = str(num5)[2:4]
                                        for num6 in nums[perm[4]]:
                                            if ends[4] == str(num6)[0:2] and str(num6)[2:4] == str(num1)[0:2]:
                                                print(num1)
                                                print(num2)
                                                print(num3)
                                                print(num4)
                                                print(num5)
                                                print(num6)
                                                print(num1 + num2 + num3 + num4 + num5 + num6)
                                                escape = True
                                                break


                                    