import re

with open('input-8.txt') as f:
    lines = [line.strip() for line in f]

def parseInstruction(instruction):
  op, val = re.findall(r'(\w+) ([-+]\d+|\d+)', instruction)[0]
  return [op, int(val)]


def executeInstruction(lineIndex, acc, instruction):
  op, val = parseInstruction(instruction)
  lineIndex +=1
  if op == 'nop':
    pass
  elif op == 'jmp':
    lineIndex += val - 1
  elif op == 'acc':
    acc += val

  return lineIndex, acc

def parseInstructions(lines):
  executedInstructions = set()
  acc, lineIndex = 0,0
  instruction = lines[lineIndex]
  instructionSet = "%s:%s"%(lineIndex, instruction )
  
  while instructionSet not in executedInstructions:

    lineIndex, acc = executeInstruction(lineIndex, acc, instruction)   
    executedInstructions.add(instructionSet)
    
    try:
      instruction = lines[lineIndex]
      instructionSet = "%s:%s"%(lineIndex, lines[lineIndex])
    except IndexError:
      break;
 
  return acc

print parseInstructions(lines)
