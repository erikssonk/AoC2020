with open('input-10.txt') as f:
  numbers = [int(line.strip()) for line in f]
#numbers = [16,10,15,5,1,11,7,19,6,12,4]

numbers.append(0)
joltages = sorted(numbers)
joltages.append(max(joltages) + 3 )

paths = {}
def findPaths(index):
  if (index==len(joltages) - 1):
    return 1

  if index in paths: 
    return paths[index]

  result = 0

  for idx in range(index+1, len(joltages)):
    diff = joltages[idx]-joltages[index]
    if diff <= 3:
      result += findPaths(idx)
  paths[index] = result
  return paths[index]

print(findPaths(0))