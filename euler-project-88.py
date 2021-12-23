#import time
#start_time = time.time()

ans = []
N = 12000
for k in range(N+1): #initialise our values with the highest value they could take. This comes from the fact that (1 + 1 + ... + 1 + 2 + n) = 1 x 1 x ... x 1 x 2 x n if there are (n-2) '1's
    ans.append(2*k)
n=0
while 2**n < N: #finding the longest possible string of 2's which multiply to less than N
    n+=1

nonones  = []
for i in range(n):
    nonones.append(2)

def listprod(numlist):
    num = 1
    for i in range(len(numlist)):
        num *= numlist[i]
    return num

def listsum(numlist):
    num = 0
    for i in range(len(numlist)):
        num += numlist[i]
    return num

keepGoing = True
while keepGoing:
    prodofnums = listprod(nonones)
    sumofnums = listsum(nonones)
    if prodofnums < 2*N: #if prod is bigger we know it isn't a solution
        k = prodofnums - sumofnums + len(nonones) # finding the number numbers involved in the sum/product (i.e counting num of required '1's)
        if k <= N:
            if ans[k] > prodofnums: #store it if it imporves on our current answer
                ans[k] = prodofnums
        nonones[-1] += 1
    else:
        i = -1
        while listprod(nonones) >= 2*N: #this while loop incriments the values in nonones so that they read in ascending order and we count all valid choices
            if -i == len(nonones): #in this case we need to reduce the length of nonones by 1
                if -i == 2:
                    keepGoing = False
                    break
                nonones.pop(-1)
                for j in range(-i-1):
                    nonones[j] = 2
                break
            nonones[i-1] += 1
            for j in range(-i):
                nonones[-1 - j] = nonones[i-1]
            i -= 1
            

ansset = set(ans)
ansset.remove(2)
total = 0
for num in ansset:
    total += num
print(total)
#print(time.time() - start_time)