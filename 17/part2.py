with open('input-17.txt') as f:
  rows = [line.strip() for line in f]

def transform(cubes):
  new = {}
  for cube in cubes:
    activeNeighbors = getActiveNeighbors(cube, cubes)
    if cubes[cube] == '#':

      new[cube] = '.'
      if activeNeighbors in [2,3]:
        new[cube] = '#'
        
      neighbors = findNeighbors(cube)
      for neighbor in neighbors:
        if neighbor not in cubes:
          if getActiveNeighbors(neighbor, cubes)  == 3:
            new[neighbor] = '#'

    elif cubes[cube] == '.':
      if activeNeighbors == 3:
        new[cube] = '#'
      else:
        new[cube] = '.'
  return new

def findNeighbors(cube):
  neighbors = []
  position = [-1,0,1]

  for x in position:
    for y in position:
      for z in position:
        for w in position:
          if not (x == 0 and y == 0 and  z== 0 and w == 0):
            neighbors.append((cube[0] + x, cube[1] + y, cube[2] + z, cube[3] + w))

  return neighbors

def getActiveNeighbors(neighbor, cubes):
  neighbors = findNeighbors(neighbor)
  total = 0

  for neighbor in neighbors:
    total += int(neighbor in cubes and cubes[neighbor] == '#')
  
  return total

cubes = {}

for y, row in enumerate(rows):
  for x, char in enumerate(list(rows[y])):
    cubes[(x,y,0, 0)] = char

for i in range(0,6):
  cubes = transform(cubes)

acitve = 0
for pos in cubes:
  if cubes[pos] == '#':
    acitve += 1

print(acitve)
   