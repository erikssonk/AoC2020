with open('input-10.txt') as f:
  numbers = [int(line.strip()) for line in f]
numbers = [16,10,15,5,1,11,7,19,6,12,4]


numbers.append(0)
joltages = sorted(numbers)
joltages.append(max(joltages) + 3 )

highDiff, lowDiff = 0, 0

for index in range(len(joltages) -1) :
  diff = joltages[index + 1 ] - joltages[index]

  if diff == 3:
    highDiff += 1

  if diff == 1:
    lowDiff +=1  
  
print highDiff, lowDiff
