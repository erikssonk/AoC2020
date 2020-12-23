cups = [3,2,7,4,6,5,1,8,9]

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

nodeDict = {i:Node(i) for i in range(1,1000001)}

for idx in range(len(cups)): 
  nodeDict[cups[idx]].next = nodeDict[cups[(idx+1) % len(cups)]]

def gameOfCups(totalCups, steps):
    cup = nodeDict[cups[0]]
    for _ in range(steps):
        picked = cup.next
        cup.next = cup.next.next.next.next
        num = cup.value
        
        while num in [cup.value, picked.value, picked.next.value, picked.next.next.value]:
            if num!=1:
              num = num - 1 
            else:
              num = totalCups
        
        dest = nodeDict[num]
        picked.next.next.next = dest.next
        dest.next = picked
        cup = cup.next

gameOfCups(len(cups), 100)

pointer, acc = nodeDict[1], ""
for _ in range(len(cups)-1):
    pointer = pointer.next
    acc += str(pointer.value)

print("Part 1: %s"%acc)
cups += list(range(10,1000001))

for idx in range(len(cups)): 
  nodeDict[cups[idx]].next = nodeDict[cups[(idx+1) % len(cups)]]

gameOfCups(1000000, 10000000)
print("Part 2: %d"%(nodeDict[1].next.value*nodeDict[1].next.next.value))