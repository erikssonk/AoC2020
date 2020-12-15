import re

with open('input-11.txt') as f:
  rows = [line.strip() for line in f]

FREECHAR = 'L'
OCCUPIEDCHAR = '#'
ALLCHARS = [FREECHAR,OCCUPIEDCHAR]

seatsMap = {}

def getAdjacents(rows, yPos, xPos, seatsMap):
  
  adjacents = []

  increment = 0
  foundSeats = {
    'high': False,
    'low': False
  }

  if "%d-%d"%(yPos,xPos) in seatsMap:
    seatMap = seatsMap["%d-%d"%(yPos,xPos)]
    for key in seatMap.keys():
      for pos in seatMap[key]:
        adjacents.append(rows[pos[0]][pos[1]])
    
    return adjacents

  seatMap = seatsMap.get("%d-%d"%(yPos,xPos), {'x': [],'y': [], 'xy': [], 'yx': []})

  while True:
    increment += 1
    pos = [yPos - increment, yPos + increment]
    if pos[0] >= 0 and not foundSeats["low"]:
      try:
        char = rows[pos[0]][xPos]
        if char in ALLCHARS:
          foundSeats["low"] = char
          seatMap['y'].append([pos[0], xPos])
          
      except:
        pass
    if not foundSeats["high"]:
      try:
        char = rows[pos[1]][xPos]
        if char in ALLCHARS:
          foundSeats["high"] = char
          seatMap['y'].append([pos[1], xPos])
          
      except:
        pass 
    if foundSeats["low"] != False and foundSeats["high"] != False:
      break

    if pos[0] < 0 and pos[1] > len(rows):
      break
  
  for key in foundSeats:
    if foundSeats[key]:
      adjacents.append(foundSeats[key])

  increment = 0
  foundSeats = {
    'high': False,
    'low': False
  }

  while True:
    increment += 1
    pos = [xPos - increment, xPos + increment]
    if pos[0] >= 0 and not foundSeats["low"]:
      try:
        char = rows[yPos][pos[0]]
        if char in ALLCHARS:
          foundSeats["low"] = char
          seatMap['x'].append([yPos, pos[0]])
      except:
        pass
    if not foundSeats["high"]:
      try:
        char = rows[yPos][pos[1]]
        if char in ALLCHARS:
          foundSeats["high"] = char
          seatMap['x'].append([yPos, pos[1]])
      except:
        pass 
    if foundSeats["low"] != False and foundSeats["high"] != False:
      break

    if pos[0] < 0 and pos[1] > len(rows):
      break

  for key in foundSeats:
    if foundSeats[key]:
      adjacents.append(foundSeats[key])

  #Left (High) to Right (Low) on XY Axis
  foundSeats = {
    'high': False,
    'low': False
  }
   
  increment = 1
  while True:
    left = [yPos - increment, xPos - increment]
    right = [yPos + increment, xPos + increment]
  
    if not foundSeats["high"] and left[0] >= 0 and left[1] >= 0 :
      try:
        char = rows[left[0]][left[1]]
        if char in ALLCHARS:
          foundSeats["high"] = char
          seatMap['xy'].append([left[0], left[1]])
      except:
        pass
    if not foundSeats["low"]:
      try:
        char = rows[right[0]][right[1]]
        if char in ALLCHARS:
          foundSeats["low"] = char
          seatMap['xy'].append([right[0], right[1]])
      except:
        pass
    if foundSeats["low"] != False and foundSeats["high"] != False:
      break
    if left[0] < 0 and left[1] < 0 and right[0] > len(rows) and right[1] > len(rows[yPos]):
      break
  
    increment +=1
    
  for key in foundSeats:
    if foundSeats[key]:
      adjacents.append(foundSeats[key])

  #Left (low) to Right (High) on XY Axis
  foundSeats = {
    'high': False,
    'low': False
  }
  
  increment = 1
  
  while True:
    left = [yPos + increment, xPos - increment]
    right = [yPos - increment, xPos + increment]
 
    if not foundSeats["low"] and left[1] >= 0:

      try:
        char = rows[left[0]][left[1]]
        if char in ALLCHARS:
          foundSeats["low"] = char
          seatMap['yx'].append([left[0], left[1]])

      except:
        pass
      
    if not foundSeats["high"] and right[0] >= 0:
    
      try:
        char = rows[right[0]][right[1]]
        if char in ALLCHARS:
          foundSeats["high"] = char
          seatMap['yx'].append([right[0], right[1]])
      except:
        pass
    if foundSeats["low"] != False and foundSeats["high"] != False:
      break
    if left[0] >= len(rows) and left[1] < 0 and right[0] < 0 and right[1] >= len(rows[yPos]):
      break
    increment +=1
  seatsMap["%d-%d"%(yPos,xPos)] = seatMap

  for key in foundSeats:
    if foundSeats[key]:
      adjacents.append(foundSeats[key])
  return adjacents

it = 1
def countAdjacents(adjacents):
  free = 0
  occupied = 0
  for adjacent in adjacents:
    if adjacent == OCCUPIEDCHAR:
      occupied += 1
    elif adjacent == FREECHAR:
      free += 1
  return free, occupied


mySet = set()

while True:
  currentRows = rows[:]

  for rowIndex in range(0,len(currentRows)):
    row = currentRows[rowIndex]
    chars = list(row)
    for charIndex in range(0,len(chars)):
      char = chars[charIndex]
      if char == ".":
        continue

      adjacents = getAdjacents(rows, rowIndex, charIndex, seatsMap)

      free, occupied = countAdjacents(adjacents)

      if char == FREECHAR and occupied == 0:
        chars[charIndex] = OCCUPIEDCHAR
      if char == OCCUPIEDCHAR and occupied >= 5:
        chars[charIndex] = FREECHAR

    currentRows[rowIndex] = "".join(chars)
  current = "".join(currentRows)
  if current in mySet:
    break;
  mySet.add(current)
  rows = currentRows[:]

print "ALL %d"%len(re.findall(r'#', current))