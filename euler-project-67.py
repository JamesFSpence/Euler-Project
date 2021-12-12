with open("euler-project-67-text-file.txt") as f:
    triangle = f.read().splitlines()

height = 100
for r in range(height):
    triangle[r] = triangle[r].split()

maxroute = [triangle[height-1]]
for r in range(height-1):
    maxroute.append([])
    for c in range(0,height-1-r):
        bigger = max(int(maxroute[r][c]),int(maxroute[r][c+1]))
        maxroute[r+1].append(str(int(triangle[height-2-r][c]) + bigger))
    
print(maxroute)