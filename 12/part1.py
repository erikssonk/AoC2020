import re

with open('input-12.txt') as f:
  positions = [line.strip() for line in f]

facing = 'E'

res = {
  'N' :0,
  'S' :0,
  'E' :0,
  'W' :0
}

turns = {
  'N' : {'R': 'E', 'L' : 'W'},
  'S' : {'R': 'W', 'L' : 'E'},
  'E' : {'R': 'S', 'L' : 'N'},
  'W' : {'R': 'N', 'L' : 'S'}
}

for position in positions:
  action, value =  re.findall(r'([A-Z])(\d+)', position)[0]

  if action in res:
    res[action] += int(value)
  elif action == 'F':
    res[facing] += int(value)
  elif action in ['R', 'L']:
    for rotation in range(0, int(value) / 90):
      facing = turns[facing][action] 

yAxis = sorted([res['N'],res['S']], reverse=True)
xAxis = sorted([res['W'],res['E']], reverse=True)
print (yAxis[0] - yAxis[1]) + (xAxis[0] - xAxis[1])