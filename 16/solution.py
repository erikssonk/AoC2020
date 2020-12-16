import re
from collections import defaultdict

ignore_words = ["your ticket:", "nearby tickets:"]

with open('input-16.txt') as f:
  i = 0
  lines = [[]]
  for line in f:
    if line == '\n':
      i += 1
      lines.append([])
      continue
    if line.strip() in ignore_words:
      continue
    lines[i].append(line.strip())

rules = defaultdict(list)
ranges = set()

for line in lines[0]:
  rulename = re.match(r"(\w+( \w+)?):", line).group(1)

  for value in re.findall(r"\d+\-\d+", line):
    rules[rulename].append(tuple(int(n) for n in value.split("-")))
    ranges.add(tuple(int(n) for n in value.split("-")))

errorRate = 0
validTickets = []

for line in lines[2]:
  ticket = [int(n) for n in line.split(",")]

  for num in ticket:
    valid = False

    for lo, hi in ranges:
      if lo <= num <= hi:
        valid = True
        break

    if not valid:
      errorRate += num
      break

  if valid:
    validTickets.append(ticket)

possibleRules = {idx: set(rules.keys()) for idx in range(len(validTickets[0]))}

for ticket in validTickets:
  for idx, value in enumerate(ticket):
    for rule in rules:
      possible = False
      
      for low, high in rules[rule]:
        if low <= value <= high:
            possible = True
            break

      if not possible:
        possibleRules[idx].discard(rule)

for idx in sorted(possibleRules, key=lambda k: len(possibleRules[k])):
  rule = next(iter(possibleRules[idx]))

  for j in possibleRules:
    if idx != j:
      possibleRules[j].discard(rule)

myTicket = [int(n) for n in lines[1][0].split(",")]
multiply = 1

for rule in possibleRules:
  if possibleRules[rule].pop().startswith("departure"):
    multiply *= myTicket[rule]

print "Part 1:", errorRate 
print "Part 2:", multiply