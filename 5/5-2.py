from math import floor, ceil

with open('input-5.txt') as f:
    boardingPasses = [line.strip() for line in f]

columnRange = 7
columnMap = {
  'L': False,
  'R': True,
}

rowRange = 127
rowMap = {
  'F': False,
  'B': True
}

def calcId(code, codeMap, codeRange):
  low = 0
  high = codeRange

  for char in code:

    current = codeMap[char]
    
    baseLine = float(high - low) / 2
    if current:
      low = low + ceil(baseLine) 
    else:
      high = high - ceil(baseLine)

  result = low
  if current:
    result = high

  return int(result)

seatIds = []
for boardingPass in boardingPasses:
  
  row = boardingPass[0:7]
  column = boardingPass[7:]
  rowId = calcId(row, rowMap, rowRange)
  columnId = calcId(column, columnMap, columnRange)
  seatId = rowId * 8 + columnId

  seatIds.append(seatId) 

seatIds = sorted(seatIds)

for index in range(0,len(seatIds)):
  seatId = seatIds[index]
  if seatId + 1 != seatIds[index +1]:
    print seatId + 1  
    exit()
