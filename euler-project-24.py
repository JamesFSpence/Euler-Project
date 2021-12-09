import itertools
count = 0
for perm in itertools.permutations(range(10)):
    count+=1
    if count == 1000000:
        print(perm)
