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
  num = 1
  for char in code:
    num += 1
    current = codeMap[char]
    
    baseLine = float(high - low) / 2
    if current:
      low = low + ceil(baseLine) 
    else:
      high = high - ceil(baseLine)
  
  baseLine = float(high - low) / 2
  
  if current:
    low = low + floor(baseLine) 
  else:
    high = high - floor(baseLine)

  result = low
  if current:
    result = high

  return int(result)

# def calcId(code, codeMap, codeRange):
 
#   low = 0
#   high = codeRange
#   for char in code:
#     if char == 'L' or char == 'F':
#       print "Lower half"
#       high = int( high - ceil(float(high - low) / 2))
#       #high = int( high - floor((high - low // 2)) )
#     else:
#       print "Upper half"
#       low = int(floor( low + float(high - low) / 2 ) )
#     print("%s - %s : %s"%(char, low, high))
  
#   result = low + floor(float(high - low) / 2)
#   print "Result: %s"%result
#   return result

def getSeatId(code):
  return int(code.replace('F',"0").replace("B","1").replace("R","1").replace("L","0"),2)

seatIds = []
for boardingPass in boardingPasses:
  
  row = boardingPass[0:7]
  column = boardingPass[7:]
  rowId = calcId(row, rowMap, rowRange)
  columnId = calcId(column, columnMap, columnRange)
  seatId = rowId * 8 + columnId
  if (seatId != getSeatId(boardingPass)):
    print "FAIL"
    print "%s = %s (row: %s)"%(seatId, getSeatId(boardingPass), rowId)
    exit()
  seatIds.append(seatId)
  # print "%s = %s"%(seatId, getSeatId(boardingPass))
  

seatIds = sorted(seatIds)

for index in range(0,len(seatIds)):
  seatId = seatIds[index]
  if seatId + 1 != seatIds[index +1]:
    print seatId + 1  
    exit()
