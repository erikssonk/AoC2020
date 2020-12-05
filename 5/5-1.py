with open('input-5.txt') as f:
    boardingPasses = [line.strip() for line in f]

columnRange = 7
columnMap = {
  'R': True,
  'L': False
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
    baseLine = (high - low) // 2
    if current:
      low = low + baseLine + 1
    else:
      high = high - baseLine - 1

  return low + ((high - low) // 2) 

seatIds = []
for boardingPass in boardingPasses:
  
  row = boardingPass[0:6]
  column = boardingPass[7:]
  rowId = calcId(row, rowMap, rowRange)
  columnId = calcId(column, columnMap, columnRange)
  seatIds.append(rowId * 8 + columnId)

print sorted(seatIds)[-1]


  