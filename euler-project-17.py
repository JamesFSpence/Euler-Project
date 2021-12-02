units = [0,3,3,5,4,4,3,5,5,4]
tens = [0,3,6,6,5,5,5,7,6,6]
teens = [3,6,6,8,8,7,7,9,8,8]
sum = 0

for i in range(1,1001):
    j = str(i)
    if len(j)<3:
        if len(j) == 2:
            if j[0] == '1':
                chars = teens[int(j[1])]
            else:
                chars = units[int(j[1])] + tens[int(j[0])]
        else:
            chars = units[int(j[0])]
    elif len(j) == 4:
        chars = 11
        print('Hooray!')
    else:
        if j[1] == '1':
            teenchars = teens[int(j[2])]
        else:
            teenchars = units[int(j[2])] + tens[int(j[1])]
        if j[2] == '0' and j[1] == '0':
            chars = teenchars + units[int(j[0])] + 7
            
        else:
            chars = teenchars + units[int(j[0])] + 10
            
    sum += chars
    chars = 0
print(sum)