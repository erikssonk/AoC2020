with open('input-6.txt') as f:
    answers = [line.strip() for line in f]

groupIndex = 0
groups = {}
for person in answers:
  if person == '':
    groupIndex += 1
    continue

  group = groups.setdefault(groupIndex, [])
  
  group.append(person)
  groups[groupIndex] = group

questions = {}
for groupIndex in groups:
  persons = groups[groupIndex]
  
  answer = persons[0]
  counter = set()
    
  for char in answer:
    counter.add(char)
    for person in persons:
      if not char in person:
        try:
          counter.remove(char)
        except KeyError:
          pass
  
  questions[groupIndex] = counter


num = 0
for index in questions:
  num += len(questions[index])
  
print num