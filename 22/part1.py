players = {}
with open('input-22.txt') as f:
  player = None
  for raw in f:
    raw = raw.strip()
    if len(raw) == 0: 
      continue
    
    if raw.startswith('Player'):
      player = raw.replace(':','')
      continue

    cards = players.get(player, [])
    cards.append(int(raw))
    players[player] = cards

for key in players:
  players[key] = players[key][::-1]

winningHand = []
while True:
  cards = []
 
  cards.append(players['Player 1'].pop())
  cards.append(players['Player 2'].pop())

  if cards[0] > cards[1]:
    cardOne = cards[0]
    cardTwo = cards[1]
    player='Player 1'

  elif cards[1] > cards[0]:
    cardOne = cards[1]
    cardTwo = cards[0]
    player='Player 2'
  
  players[player] = [cardTwo, cardOne] + players[player]

  if len(players['Player 1']) == 0 or len(players['Player 2']) == 0:
    winningHand = players[player]
    break; 

score = 0
for idx, number in enumerate(winningHand):
  score += number * (idx + 1)

print 'Part 1: %s won with a score of %d'%(player, score)