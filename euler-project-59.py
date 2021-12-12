with open("euler-project-59-text-file.txt") as f:
    text = f.read()
letters = text.split(',')
letterssplit = [[],[],[]]
maxcount = [0,0,0]
maxnum = [0,0,0]
i = 0
for letter in letters:
    letterssplit[i].append(int(letter))
    i+=1
    if i == 3:
        i = 0

for i in range(3):
    letterssplit[i] = sorted(letterssplit[i])
    for num in letterssplit[i]:
        if letterssplit[i].count(num)>maxcount[i]:
            maxcount[i] = letterssplit[i].count(num)
            maxnum[i] = num

key = [char^32 for char in maxnum] #assuming space (ASCII = 32) to be the most common character in each position mod 3

message = ''
print([chr(a) for a in key])
i = 0
sum = 0
for letter in letters:
    message += chr(int(letter) ^ key[i])
    sum += int(letter)^key[i]
    i+=1
    if i == 3:
        i = 0
    
print(message)
print(sum)