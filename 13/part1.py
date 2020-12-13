import re
from math import ceil

with open('input-13.txt') as f:
  data = [line.strip() for line in f]

earliest, table = data
busIds = re.findall(r'(\d+)', table)
earliest = float(int(earliest))

busTimes = {}
for busId in busIds:
  busId = float(int(busId))
  departingTime = ceil(earliest / busId) * busId
  timeDiff = departingTime - earliest
  busTimes[int(timeDiff)] = int(busId)
  
print busTimes[min(busTimes.keys())] * min(busTimes.keys())
