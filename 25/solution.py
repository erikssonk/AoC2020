def loopSize(pub, dividing):
  loop_size = 1
  while True:
    if pow(7, loop_size, dividing) == pub:
      return loop_size
    loop_size += 1

doorPub = 11239946
cardPub = 10464955
dividing = 20201227

print pow(doorPub, loopSize(cardPub, dividing), dividing)