import re

with open('input-18.txt') as f:
  lines = [line.strip() for line in f]


def evalEquation(idx, current):
  acc = 0
  op = '+'

  while idx < len(current):
    if current[idx] == ' ':
      idx += 1
    
    elif current[idx].isdigit():
      if op == '+':
        acc += int(current[idx])
      else:
        acc *= int(current[idx])
      idx += 1   

    elif current[idx] in  ['+','*']:
      op = current[idx]
      idx += 1
    
    elif current[idx] == '(':
      idx += 1
      res, idx = evalEquation(idx, current)
      if op == '+':
        acc += res
      else:
        acc *= res
    else: 
      idx += 1
      break

  return acc, idx

result = []
for line in lines:
  result.append(evalEquation(0, line)[0])
print 'Part1: ', sum(result)

    
  

