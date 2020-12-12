import re

with open('input-12.txt') as f:
  positions = [line.strip() for line in f]

facing = 'E'

ship = {
  'N' :0,
  'S' :0,
  'E' :0,
  'W' :0
}

waypoint = {
  'N' :1,
  'S' :0,
  'E' :10,
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

  if action in waypoint:
    waypoint[action] += int(value)
  elif action == 'F':
    for key in ship.keys():
      ship[key] += waypoint[key] * int(value)
  elif action in ['R', 'L']:
    storedWaypoint = dict(waypoint)
    for rotation in range(0, int(value) / 90):
      facing = turns[facing][action]    
    
    for key in storedWaypoint.keys():
      newPos = key
      for rotation in range(0, int(value) / 90):
        newPos = turns[newPos][action]
     
      waypoint[newPos] = storedWaypoint[key]

yAxis = sorted([ship['N'],ship['S']], reverse=True)
xAxis = sorted([ship['W'],ship['E']], reverse=True)
print (yAxis[0] - yAxis[1]) + (xAxis[0] - xAxis[1])