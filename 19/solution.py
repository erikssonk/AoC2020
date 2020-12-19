from lark import Lark, LarkError

with open('input-19.txt') as f:
  lines = [line.strip() for line in f]

rules = ""
for idx, line in enumerate(lines):
  if line == '':
    break
  rules += "\n%s"%line

messages = lines[idx + 1:]

def replaceChars(string, chars, replaceChars):
  for idx, char in enumerate(list(chars)):
    string = string.replace(char, replaceChars[idx])
  return string

def parseMessages(rules, messages, replaceRules = False):
  if replaceRules:
    rules = rules.replace('8: 42', '8: 42 | 42 8')
    rules = rules.replace('11: 42 31', '11: 42 31 | 42 11 31')
  
  rules = replaceChars(rules, '0123456789', 'abcdefghij')

  parser = Lark(rules, start='a')

  total = 0
  for message in messages:
    try:
      parser.parse(message)
      total += 1
    except LarkError:
      pass
  return total
print("Part 1: %s"%parseMessages(rules.strip(), messages))
print("Part 2: %s"%parseMessages(rules.strip(), messages, True))
