import re

with open('input-7.txt') as f:
    lines = [line.strip() for line in f]

colours = r'([a-zA-Z ]+) bag'
count = r'(\d+)'

bags = {}
for line in lines:
  currentColour = None 
  foundBags = re.findall(colours, line)
  
  numbers = re.findall(count, line)

  if len(numbers) == 0:
    continue
 
  bag = bags.setdefault(foundBags[0], [])

  for index in range(0, len(foundBags)):
    colour = foundBags[index]
    if not colour.startswith(' ',0):    
      continue
    
    bag.append({
      colour.strip(): int(numbers[index-1])
      })
 
  bags[foundBags[0]] = bag

totalBags = 0

def countBags(colour):
  currentSum = 1
  if not colour in bags.keys():
    return currentSum
  
  for bag in bags[colour]:
    subColour = bag.keys()[0]
    amount = bag[subColour]
    noOfBags = countBags(subColour)
    currentSum += amount * noOfBags

  return currentSum

for bag in bags['shiny gold']:
  colour = bag.keys()[0]
  amount = bag[colour]
    
  noOfBags = countBags(colour)
  
  if noOfBags == 0:
    totalBags += amount
    continue
    
  totalBags += amount * noOfBags

print totalBags