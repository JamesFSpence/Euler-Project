N = 100

yes_one = [] #number of summations to n including a 1
no_one = [] #[n][k] is the number of ways to make n using k numbers

for i in range(N+1):
    elt1 = [str(i)]
    elt2 = [str(i)]
    for j in range(i):
        elt1.append(0)
        elt2.append(0)
    no_one.append(elt1)
    yes_one.append(elt2)

for n in range(1,N+1):
    if n != 1:
        yes_one[n][1] = 0
        no_one[n][1] = 1
    else:
        yes_one[n][1] = 0
        no_one[n][1] = 1
    for k in range(2,n+1):
        yes_one[n][k] = yes_one[n-1][k-1] + no_one[n-1][k-1]
        #print(yes_one[n][k])
        #print('For K: ' + str(k) + ', N: ' + str(n))
        if k>n/2:
            no_one[n][k] = 0
        else:    
            no_one[n][k] = no_one[n-k][k]+ yes_one[n-k][k]

sum = 0
for i in range(1,N):
    sum+= yes_one[N][i] + no_one[N][i]

print(sum)