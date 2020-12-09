import random
with open('input-9.txt') as f:
    numbers = [int(line.strip()) for line in f]

def contains(value, preambleRange):
  for i in range(len(preambleRange)):
    for j in range(i, len(preambleRange)):
      if preambleRange[i] + preambleRange[j] == value:
        return True

  return False

def findInvalidNumber(numbers, preamble):
  preambleRange = numbers[0:preamble]

  for i in range(preamble, len(numbers)):
    if not contains(numbers[i], preambleRange):
      return numbers[i]
      
    preambleRange = preambleRange[1:] + [numbers[i]]

#print findInvalidNumber(numbers, preamble)
  