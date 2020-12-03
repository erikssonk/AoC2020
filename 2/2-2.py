with open('input-2.txt') as f:
    lines = [line.rstrip() for line in f]

valids = 0 

for line in lines:
  code = line.split(':')
  context = code[0].split(' ')
  firstPos, secondPos = context[0].split('-')
  char = context[1].strip()
  password = code[1].strip()

  if (password[int(firstPos)-1] == char) ^ (password[int(secondPos)-1] == char):
    valids += 1
  

print valids