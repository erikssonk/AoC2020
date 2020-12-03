with open('input-3.txt') as f:
    lines = [line.rstrip() for line in f]

xPos, foundTrees, maxX = 0, 0, len(lines[0]) - 1

for yPos in range(0,len(lines)):
  currentX = xPos + 3
  
  if currentX >= maxX:
    currentX =  currentX - maxX - 1

  xPos = currentX
  
  try:
    foundTrees += int(lines[yPos + 1][xPos] == "#")

  except IndexError:
    break;

print foundTrees