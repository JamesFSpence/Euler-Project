with open('euler-project-22-text-file.txt') as f:
    lines = f.read()

namesstring = (lines.replace('"','')).lower()
names = namesstring.split(',')
orderednames = sorted(names)
total = 0

for name in orderednames:
    lettervalues = 0
    for i in range(len(name)):
        lettervalues += (ord(name[i])-96)
    namescore = lettervalues*(orderednames.index(name)+1)
    total += namescore
    if name == 'colin':
        print(lettervalues)
        print(orderednames.index(name)+1)
        print(namescore)

print(total)