with open('input-3.txt') as f:
    lines = [line.rstrip() for line in f]

treesPerPath = {}
steps = [[1,1],[3,1], [5,1], [7,1],[1,2]]

for index in range(0,len(steps)):
  
  xChange, yChange = steps[index]
  offset = 0

  for yPos in range(0, len(lines), yChange):
    
    foundTrees = treesPerPath.setdefault(index, 0)
    treesPerPath[index] = foundTrees + int(lines[yPos][offset % len(lines[yPos])] == "#")
    offset += xChange

product = 1
for index in treesPerPath:    
  product = product * treesPerPath[index]

print product
print treesPerPath