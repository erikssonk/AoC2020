import re, math
from collections import defaultdict

def matches(t1,t2):
  t1r = ''.join([t[-1] for t in t1])
  t2r = ''.join([t[-1] for t in t2])
  t1l = ''.join([t[0] for t in t1])
  t2l = ''.join([t[0] for t in t2])
  
  t1_edges = [t1[0] , t1[-1]  ,t1r , t1l]
  t2_edges = [t2[0] , t2[-1] , t2[0][::-1] , t2[-1][::-1] , t2l , t2l[::-1] ,t2r , t2r[::-1]]

  for et1 in t1_edges:
    for et2 in t2_edges:
      if et1 == et2:
        return True
  return False

def rotate(t):
  chars = [[x[idx] for x in t] for idx in range(len(t[0]))]
  reverse = []
  for char in chars:
    reverse.append("".join(char[::-1]))
  
  return reverse


def setCorner(cor , right , down):
  rr = ''.join([t[-1] for t in right])
  dr = ''.join([t[-1] for t in down])
  rl = ''.join([t[0] for t in right])
  dl = ''.join([t[0] for t in down])
  
  r_edges = [right[0] , right[-1] , right[0][::-1] , right[-1][::-1] , rr , rr[::-1] , rl , rl[::-1]]
  d_edges = [down[0] , down[-1] , down[0][::-1] , down[-1][::-1] , dr , dr[::-1] , dl , dl[::-1]]

  for _ in range(2):
    cor = cor[::-1]
    for _ in range(4):
      cor = rotate(cor)
      if cor[-1] in d_edges and ''.join([t[-1] for t in cor]) in r_edges:
        return cor

  return None

def removeBorder(tile):
  return [x[1:-1] for x in tile[1:-1]]

def leftEdge(t1,t2):
  ref = ''.join([t[-1] for t in t1])

  for _ in range(2):
    t2 = t2[::-1]
    for _ in range(4):
      t2 = rotate(t2)
      if ''.join([t[0] for t in t2]) == ref :
        return t2
  return None

def upperEdge(t1,t2):
  ref = t1[-1]
  for _ in range(2):
    t2 = t2[::-1]
    for _ in range(4):
      t2 = rotate(t2)
      if t2[0] == ref :
        return t2
  return None

def assembleImage(img,tiles):
  
  whole_image = []
  for l in img:
    sliced = [''] * len(tiles[l[0]])
    for t in l:
      for idx,slice in enumerate(tiles[t]):
        sliced[idx] += slice
    for slice in sliced:
      whole_image.append(slice)

  return whole_image

tiles =  defaultdict(list)

with  open('input-20.txt') as f:
  for line in f:
    if 'Tile' in line :
      tile = int(re.findall(r'\d+', line)[0])
    elif '.' in line or '#' in line:
      tiles[tile].append(line.strip())

connected = defaultdict(set)

for i in tiles :
  for t in tiles :
    if i == t : continue
    if matches(tiles[i],tiles[t]) :
      connected[i].add(t)
      connected[t].add(i)

sz = int(math.sqrt(len(connected)))
image = [[0 for _ in range(sz)]for _ in range(sz)]
for i in connected:
  if len(connected[i]) == 2:
    corner = i
    break

image[0][0] = corner
added = {corner}

for y in range(1,sz):
  pos = connected[image[0][y-1]]
  for cand in pos :
    if cand not in added and len(connected[cand]) < 4:
      image[0][y] = cand
      added.add(cand)
      break

for x in range(1,sz):
  for y in range(sz):
    pos = connected[image[x-1][y]]
    for cand in pos :
      if cand not in added:
        image[x][y] = cand
        added.add(cand)
        break

tiles[image[0][0]] = setCorner(tiles[image[0][0]] , tiles[image[0][1]] , tiles[image[1][0]])

for idx,frame in enumerate(image):
  if idx != 0 :
    prv = image[idx - 1][0]
    tiles[frame[0]] = upperEdge(tiles[prv] , tiles[frame[0]])

  for x,tile in enumerate(frame):
    if x != 0 :
      prv = image[idx][x-1]
      tiles[tile] = leftEdge(tiles[prv] , tiles[tile])

for t in tiles:
  tiles[t] = removeBorder(tiles[t])

image = assembleImage(image,tiles)

ky = 0
nessi = set()
for l in open('nessi.txt').read().split('\n'):
  kx = len(l)
  for i,ch in enumerate(l):
    if ch == '#':
      nessi.add((i,ky))
  ky += 1

for _ in range(2):
  image = image[::-1]
  for _ in range(4):
    image = rotate(image)

    for x in range(0,len(image)-kx):
      for y in range(0,len(image)-ky):
        parts = [] 
        for i,p in enumerate(nessi):
          dx = x + p[0]
          dy = y + p[1]
          parts.append(image[dy][dx] == '#')
        if all(parts) :
          for part in nessi:
            dx = x + part[0]
            dy = y + part[1]
            image[dy] = image[dy][ : dx] + 'O' + image[dy][ dx +1 :]

print(sum([l.count('#') for l in image]))