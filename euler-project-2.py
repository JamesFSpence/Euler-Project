a = 1
b = 1
total = 0
while b<4000000:
    if b%2 == 0:
        total += b
    b = a+b
    a = b-a
print(total)