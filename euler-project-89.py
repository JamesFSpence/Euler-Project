with open("euler-project-89-text-file.txt") as f:
    nums = f.read().splitlines()
lettervalues = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
diff = 0
for num in nums:
    total = 0
    values = []
    l = len(num)
    for i in range(l):
        values.append(lettervalues[num[i]])
        if i != 0:
            if values[i] > values[i-1]:
                values[i] = values[i]-values[i-1]
                values[i-1] = 0
    for i in range(l):
        total += values[i]
    numofletters = 0
    x = str(total)[:-3]
    if x != '':
        numofletters += int(x)
    for char in str(total)[-3::]:
        if char == '4' or char == '9':
            numofletters += 2
        elif int(char) > 4:
            numofletters += int(char) - 4
        else:
            numofletters += int(char)
    diff += l - numofletters

print(diff)