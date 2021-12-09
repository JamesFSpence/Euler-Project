triangles = {1}

for i in range(2,100):
    triangles.add(int(i*(i+1)/2))

with open('euler-project-42-text-file.txt') as f:
    lines = f.read()

wordsstring = (lines.replace('"','')).lower()
words = wordsstring.split(',')
count = 0

for word in words:
    lettervalues = 0
    for i in range(len(word)):
        lettervalues += (ord(word[i])-96)
    if lettervalues in triangles:
        count+=1

print(count)