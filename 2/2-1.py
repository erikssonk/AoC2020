with open('input-2.txt') as f:
    lines = [line.rstrip() for line in f]

def findAllChars(needle, hay):
  index = -1
  while True:
    index = hay.find(needle, index + 1)
    if index == -1:
      break
    yield index

valids = 0 

for line in lines:
  code = line.split(':')
  premises = code[0].split(' ')
  firstChar, secondChar = premises[0].split('-')
  char = premises[1].strip()
  password = code[1].strip()

  instances = []
  for indexOfChar in findAllChars(char, password):
    instances.append(indexOfChar)
  
  instancesFound = len(instances)

  if int(firstChar) <= instancesFound and int(secondChar) >= instancesFound:
    valids += 1

print "valid passwords are: %s"%valids



