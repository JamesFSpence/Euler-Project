N = 1000000
totient = [0,0]
for i in range(2,N+1):
    totient.append(i)
print('done')
sum = 0
for i in range(2,N+1):
    if totient[i] == i:
        sum += i-1
        j = 2*i
        while j < N+1:
            totient[j]*=1-1/i
            j+=i
    else:
        sum += totient[i]

print(sum)