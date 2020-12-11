import re

with open('input-11.txt') as f:
  rows = [line.strip() for line in f]

FREECHAR = 'L'
OCCUPIEDCHAR = '#'

def getAdjacents(rows, yPos, xPos):
  adjacents = []
  
  for rowIndex in range(yPos -1, yPos +2):
    if rowIndex < 0:
      continue
    if rowIndex >= len(rows):
      continue
    for charIndex in range(xPos -1, xPos +2):
      if charIndex < 0:
        continue
      if charIndex >= len(rows[rowIndex]):
        continue

      if yPos == rowIndex and xPos == charIndex:
        continue

      adjacents.append(rows[rowIndex][charIndex])
      
  return adjacents

def countadjacents(adjacents):
  free = 0
  occupied = 0
  for adjacent in adjacents:
    if adjacent ==OCCUPIEDCHAR:
      occupied += 1
    elif adjacent == FREECHAR:
      free += 1
  return free, occupied

while True:
  currentRows = rows[:]

  for rowIndex in range(0,len(currentRows)):
    row = currentRows[rowIndex]
    chars = list(row)
    for charIndex in range(0,len(chars)):
      char = chars[charIndex]
      if char == ".":
        continue

      adjacents = getAdjacents(rows, rowIndex, charIndex)
      free, occupied = countadjacents(adjacents)

      if char == FREECHAR and occupied == 0:
        chars[charIndex] = OCCUPIEDCHAR
      if char == OCCUPIEDCHAR and occupied >= 4:
        chars[charIndex] = FREECHAR

    currentRows[rowIndex] = "".join(chars)
  newRow =  "".join(currentRows)
  prevRow = "".join(rows)
  if newRow == prevRow:
    break
  rows = currentRows[:]


acc = 0
for row in rows:
  matches = re.findall(r'#', row)
  acc += len(matches)

print acc