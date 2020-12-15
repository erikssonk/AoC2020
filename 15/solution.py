import re
from math import ceil

with open('input-15.txt') as f:
  numbers = [int(x) for x in f.readline().split(',')]

i = 2
past = {}
immediate = numbers[-1]

for data in numbers[:-1]:
    past[data] = i - 1
    i = i + 1

def round(i,past,immediate):
    old = immediate
    if old in past:
        immediate = (i-1)- past[immediate]
    else:
        immediate = 0
    past[old] = i - 1
    i = i + 1
    
    return i,past,immediate

target = 2020
while i <= target:
    i,past,immediate = round(i,past,immediate)

print(immediate)

#Part 2
target = 30000000
while i <= target:
    i,past,immediate = round(i,past,immediate)

print(immediate)