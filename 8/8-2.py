# I used '-' in the name, can't import then :( Lesson learnt!
execfile('8-1.py')

with open('input-8.txt') as f:
    lines = [line.strip() for line in f]

def checkCorruptedOps(lines):
  rewriteOps = {
    'jmp' : lambda : ("jmp", "nop"),
    'nop' : lambda : ("nop", "jmp")
    }

  acc = 0
  for lineIndex in range(1, len(lines)):
    instruction = lines[lineIndex]
    op, _ = parseInstruction(instruction)
    if op not in rewriteOps:
      continue
    
    replaceOp = rewriteOps[op]()
    
    adjustedLines = lines[:]
    adjustedLines[lineIndex] = instruction.replace(replaceOp[0], replaceOp[1])
 
    acc, terminated = parseInstructions(adjustedLines)  
  
    if terminated:
      return acc
   
print checkCorruptedOps(lines)