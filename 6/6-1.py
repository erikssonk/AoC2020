with open('input-6.txt') as f:
    answers = [line.strip() for line in f]

questions = {}
group = 1

for person in answers:
  if person == '':
    group += 1
    continue
  question = questions.setdefault(group, set())
  
  for char in person: 
    question.add(char)
  
  questions[group] = question

num = 0
for index in questions:
  num += len(questions[index])

print num
  
