with open('input-24.txt') as f:
  lines = []
  for line in f:
    line = line.strip()
    steps = []
    while line != '':
      if line[0] in ['e','w']:
        steps += [line[0]]
        line = line[1:]
      else:
        steps += [line[:2]]
        line = line[2:]
    lines.append(steps)

def walk(steps):
  pos = [0,0]
  for direction in steps:
    if direction == 'e': 
      pos[0] += 2
      
    if direction == 'w': 
      pos[0] += -2

    if direction == 'ne':
      pos[0] += 1
      pos[1] += 1

    if direction == 'nw':
      pos[0] += -1
      pos[1] +=1

    if direction == 'se':
      pos[0] += 1
      pos[1] += -1

    if direction == 'sw':
      pos[0] += -1
      pos[1] += -1

  return (pos[0], pos[1])

hexagons = {}

for line in lines:
  position = walk(line)
  
  if position in hexagons:
    if bool(hexagons[position]):
      hexagons[position] = 0
    else:
      hexagons[position] = 1
  else:
    hexagons[position] = 1

def getBlackHexagons(hexagons):
  black = 0
  for hexagon in hexagons:
    black += hexagons[hexagon]
  return black

print('Part1: %d'%getBlackHexagons(hexagons))

def setNeighbors(hexagon,hexagons):
  xPos,yPos = [2,-2,1,-1,1,-1],[0,0,1,1,-1,-1]
  newHexagons = {}
  for num in range(6):
    x,y = hexagon[0] + xPos[num], hexagon[1] + yPos[num]
    if not (x,y) in hexagons:
      newHexagons[(x,y)] = 0
  return newHexagons

def getNeighbors(hexagon,hexagons):
  numNeighbors = 0
  xPos,yPos = [2,-2,1,-1,1,-1],[0,0,1,1,-1,-1]
  for num in range(6):
    x,y = hexagon[0] + xPos[num], hexagon[1] + yPos[num]
    if (x,y) in hexagons and hexagons[(x,y)] == 1: 
      numNeighbors += 1
  return numNeighbors

def day(hexagons):
  newHexagons = dict(hexagons)
  for hexagon in hexagons:
    neighbors = getNeighbors(hexagon, hexagons)
    if hexagons[hexagon] == 1 and neighbors in [0,3,4,5,6]:
      newHexagons[hexagon] = 0
    elif hexagons[hexagon] == 0 and neighbors == 2:
      newHexagons[hexagon] = 1
  return newHexagons

for _ in range (100):
  neighbors = {}
  for hexagon in hexagons:
    newHexagon = setNeighbors(hexagon,hexagons)
    for h in newHexagon:
      neighbors[h] = newHexagon[h]
  for n in neighbors:
    if not n in hexagons:
      hexagons[n] = neighbors[n]
  hexagons = day(hexagons)

print('Part2: %d'%getBlackHexagons(hexagons))