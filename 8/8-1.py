import re

with open('input-8.txt') as f:
    lines = [line.strip() for line in f]

def parseLine(line):
  cmd, num = re.findall(r'(\w+) ([-+]\d+)', line)[0]
  return [cmd, int(num)]

runCmds = set()

acc = 0
lineNo = 0
identifier = ''

while identifier not in runCmds:
  
  line = lines[lineNo]
  identifier = "%d:%s"%(lineNo,lines[lineNo])
  runCmds.add(identifier)

  cmd, num = parseLine(line)

  lineNo += 1

  if cmd == 'acc':
    acc += num

  if cmd == 'jmp':
    lineNo += num - 1
    
  line = lines[lineNo]
  identifier = "%d:%s"%(lineNo,lines[lineNo])
  
print acc
