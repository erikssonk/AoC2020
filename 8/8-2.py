import re

with open('input-8.txt') as f:
    lines = [line.strip() for line in f]

runCmds = []

def parseLine(line):
  cmd, num = re.findall(r'(\w+) ([-+]\d+)', line)[0]
  return [cmd, int(num)]


def interpreter(lines): 
  acc = 0
  lineNo = 0
  runCmds = set()
  identifier = "%d:%s"%(lineNo,lines[lineNo])
  while identifier not in runCmds:
    runCmds.add(identifier)

    line = lines[lineNo]
   
    cmd, num = parseLine(line)

    lineNo += 1

    if cmd == 'acc':
      acc += num

    if cmd == 'jmp':
      lineNo += num - 1

    if len(lines) == lineNo:
      return acc, True      
    line = lines[lineNo]
    
    identifier = "%d:%s"%(lineNo,lines[lineNo])
    
    if identifier in runCmds:
      return acc, False
  
  return acc, True

def fixCorruptedCmd(lines):
  acc = 0
  lineNo = 0
  currentLines = lines[:]
  for lineNo in range(1, len(currentLines)):
    cmd, num = parseLine(currentLines[lineNo])
    if cmd == 'nop':
      cmd = 'jmp'
    elif cmd == 'jmp':
      cmd = 'nop'

    adjustedLines = lines[:]

    strNum = str(num)
    if num >= 0:
      strNum = "+%s"%num

    adjustedLines[lineNo] = " ".join([cmd, strNum])
    
    acc, valid = interpreter(adjustedLines)
    
    if valid:
      return acc

print fixCorruptedCmd(lines)