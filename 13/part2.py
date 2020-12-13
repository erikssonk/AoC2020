import re
from math import ceil

with open('input-13.txt') as f:
  data = [line.strip() for line in f]

# http://python.algorithmexamples.com/web/blockchain/chinese_remainder_theorem.html !
def extended_euclid(a, b):
    """
    >>> extended_euclid(10, 6)
    (-1, 2)
 
    >>> extended_euclid(7, 5)
    (-2, 3)
 
    """
    if b == 0:
        return (1, 0)
    (x, y) = extended_euclid(b, a % b)
    k = a // b
    return (y, x - k * y)

# Uses ExtendedEuclid to find inverses
def chinese_remainder_theorem(busses):
    """
    >>> chinese_remainder_theorem(5,1,7,3)
    31
 
    Explanation : 31 is the smallest number such that
                (i)  When we divide it by 5, we get remainder 1
                (ii) When we divide it by 7, we get remainder 3
 
    >>> chinese_remainder_theorem(6,1,4,3)
    14
 
    """
    bus, time = busses[0]
    for nextBus, offset in busses[1:]:
      m1, m2 = extended_euclid(bus, nextBus)
      time = time * m2 * nextBus + offset * m1 * bus
      bus = bus * nextBus
      time %= bus
    
    return time


def findLowestTimestamp(table):
  busses = []
  print table.split(',')
  for bus in table.split(','):
    if bus == "x":
      busses.append(0)
      continue
    busses.append(int(bus))

  modulosBuses = []
  
  for i, bus in enumerate(busses):
    if bus > 0:
      modulosBuses.append([bus, (bus - i) % bus])
  
  print chinese_remainder_theorem(modulosBuses)
  
findLowestTimestamp(data[1])
# 1068781