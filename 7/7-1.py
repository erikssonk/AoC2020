import re

with open('input-7.txt') as f:
    lines = [line.strip() for line in f]

contains = r'contain no other'
colours = r'([a-zA-Z ]+) bag'

bags = {}
for line in lines:
  currentColour = None 
  foundBags = re.findall(colours, line)
  
  if re.findall(contains, foundBags[0]):
    continue

  bag = bags.setdefault(foundBags[0], [])
  for colour in foundBags:
    if not colour.startswith(' ',0):    
      continue
    
    bag.append(colour.strip())
  
  bags[foundBags[0]] = bag

myColour = "shiny gold"
found = 0

def lookInBag(colour, lookFor):
  try:
    bag = bags[colour]
  except KeyError:
    return False
  
  if (lookFor in bag):
    return True
  
  for bagColour in bag:
    result = lookInBag(bagColour, lookFor)    
    if result:
      return result

  return False

for bagColour in bags.keys():
  currentColours = bags[bagColour]

  if (myColour in currentColours):
    found +=1
    continue

  for colour in currentColours:
    result = lookInBag(colour, myColour)
    if result:
      found += int(result)
      break;


print found
    