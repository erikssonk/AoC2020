with open('input-1.txt') as f:
    inputs = [int(line.rstrip()) for line in f]

sortedInputs = sorted(inputs)

print "1-1\n"
for firstNum in sortedInputs:
  for secondNum in sortedInputs:
    sumOfThem = firstNum + secondNum
    if sumOfThem >= 2020:
        break
  if sumOfThem == 2020:
    print "%d*%d=%d"%(firstNum, secondNum, firstNum * secondNum)
    break;

print "1-2\n"
for firstNum in sortedInputs:
  for secondNum in sortedInputs:
    for thirdNum in sortedInputs:
      sumOfThem = firstNum + secondNum + thirdNum
      if sumOfThem >= 2020:
        break
    if sumOfThem == 2020:
      break

  if sumOfThem == 2020:
    print "%d*%d*%d=%d"%(firstNum, secondNum, thirdNum, firstNum * secondNum * thirdNum)
    break;

