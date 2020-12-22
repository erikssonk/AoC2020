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

def game(playerOne, playerTwo):
  gameState = set()
  while len(playerOne) > 0 and len(playerTwo) > 0:
    currentState = tuple(playerOne + [' -|- '] + playerTwo)
    if currentState in gameState:
      return [1],[0]

    cards = []
    gameState.add(currentState)
    cards.append(playerOne.pop())
    cards.append(playerTwo.pop())

    if len(playerOne) >= cards[0] and len(playerTwo) >= cards[1]:

      subCards = game(playerOne[::-1][:cards[0]][::-1], playerTwo[::-1][:cards[1]][::-1])
      if subCards[0]:
        playerOne = [cards[1], cards[0]] + playerOne
      elif subCards[1]:
        playerTwo = [cards[0], cards[1]] + playerTwo    
    elif cards[0] > cards[1]:
      playerOne = [cards[1], cards[0]] + playerOne

    elif cards[1] > cards[0]:
      playerTwo = [cards[0], cards[1]] + playerTwo
  
  return playerOne, playerTwo

playerOne, playerTwo =  game(players['Player 1'], players['Player 2'])

winningHand = playerOne
player = 'Player 1'
if playerTwo:
  winningHand = playerTwo  
  player = 'Player 2'

score = 0

for idx, number in enumerate(winningHand):
  score += number * (idx + 1)

print 'Part2: %s won with a score of %d'%(player, score)