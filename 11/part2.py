import re

with open('input-11.txt') as f:
  rows = [line.strip() for line in f]

FREECHAR = 'L'
OCCUPIEDCHAR = '#'
ALLCHARS = [FREECHAR,OCCUPIEDCHAR]

def getAdjacents(rows, yPos, xPos, it):
  
  adjacents = []
  debug = it == 2 and yPos == 1 and xPos == 1

  # if debug:
  #   print "Debug enabled!!"
  #   print yPos, xPos
  # Y axis
  yIncrement = 1
  foundSeats = {
    'high': False,
    'low': False
  }
  while True:
    if not foundSeats["high"]:
      try:
        char = rows[yPos + yIncrement][xPos]
        if char in ALLCHARS:
          foundSeats["high"] = char
      except:
        pass

    if yPos - yIncrement > -1 and not foundSeats["low"]:
      try:
        char = rows[yPos - yIncrement][xPos]
        if char in ALLCHARS:
          foundSeats["low"] = char
      except:
        pass

    if yPos - yIncrement < 0 and yPos + yIncrement >= len(rows[yPos]):
      break

    yIncrement += 1

  for key in foundSeats:
    if foundSeats[key]:
      adjacents.append(foundSeats[key])

  # X axis
  xIncrement = 1
  foundSeats = {
    'high': False,
    'low': False
  }
  while True:
    if not foundSeats["high"]:
      try:
        char = rows[yPos][xPos + xIncrement]
        if char in ALLCHARS:
          foundSeats["high"] = char
      except:
        pass

    if xPos - xIncrement >= 0 and not foundSeats["low"]:
      try:
        char = rows[yPos][xPos - xIncrement]
        if char in ALLCHARS:
          foundSeats["low"] = char
      except:
        pass
    if xPos - xIncrement < 0 and xPos + xIncrement >= len(rows):
      break

    xIncrement += 1

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
      except:
        pass
    if not foundSeats["low"]:
      try:
        char = rows[right[0]][right[1]]
        if char in ALLCHARS:
          foundSeats["low"] = char
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

      except:
        pass
      
    if not foundSeats["high"] and right[0] >= 0:
    
      try:
        char = rows[right[0]][right[1]]
        if char in ALLCHARS:
          foundSeats["high"] = char
      except:
        pass
    if foundSeats["low"] != False and foundSeats["high"] != False:
      break
    if left[0] >= len(rows) and left[1] < 0 and right[0] < 0 and right[1] >= len(rows[yPos]):
      break
    increment +=1

  for key in foundSeats:
    if foundSeats[key]:
      adjacents.append(foundSeats[key])
  return adjacents

it = 1
def countAdjacents(adjacents):
  free = 0
  occupied = 0
  for adjacent in adjacents:
    if adjacent ==OCCUPIEDCHAR:
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

      adjacents = getAdjacents(rows, rowIndex, charIndex, it)
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