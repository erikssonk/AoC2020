execfile('9_1.py')

with open('input-9.txt') as f:
    numbers = [int(line.strip()) for line in f]

def findWeakness(numbers, value):     
  numberLength = len(numbers)
  for i in range(numberLength):
    for j in range(i, numberLength):
      numberRange = numbers[i:j]
      total = sum(numberRange)

      if total > value:
        break

      if total == value:
        return min(numberRange) + max(numberRange)

invalidNumber = findInvalidNumber(numbers, 25)

print findWeakness(numbers, invalidNumber)
  