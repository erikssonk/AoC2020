import collections
import re

tiles = {}
with open('input-20.txt') as f:
  for line in f:
    line = line.strip()
    rawTileId = re.findall(r'Tile (\d+):', line)
    if (len(rawTileId) == 1):
      tileId = int(rawTileId[0])
      continue
    if len(line) == 0:
      continue
    tile = tiles.get(tileId, [])
    tile.append(line)
    tiles[tileId] = tile

def getEdges(image):
  e = [image[0], image[-1], ''.join(row[0] for row in image), ''.join(row[-1] for row in image)]
  return e + [e_i[::-1] for e_i in e]


edges = []
for tile in tiles.values():
  for idx in getEdges(tile):
    edges.append(idx)

edgeCounts = collections.Counter(edges)

corners = {}
for tileId in tiles.keys():
  for idx in getEdges(tiles[tileId]):
    if edgeCounts[idx] > 1:
      corner = corners.get(tileId, [])
      corner.append(idx)
      corners[tileId] = corner

cornerIds = sorted(tiles, key=lambda tileId: sum(1 for idx in corners[tileId]))[:4]

product = 1
for cornerId in cornerIds:
  product *= cornerId

print product