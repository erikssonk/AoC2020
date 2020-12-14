import re
from math import ceil

with open('input-14.txt') as f:
  lines = [line.strip() for line in f]

part1, part2, mask = {}, {},{}

for line in lines:
    if line.startswith('mask'):
        mask = {idx: bit for idx, bit in enumerate(line.split()[-1])}
        continue

    address, value = list(map(int, re.findall(r'-?\d+', line)))
    binValue = list(bin(value)[2:].rjust(36, '0'))

    for key, bit in mask.items():
        if bit != 'X':
            binValue[key] = bit

    address = bin(address)[2:].rjust(36, '0')
    part1[address] = int(''.join(binValue), 2)

    addresses = [list(address)]

    for key, val in mask.items():
        if val == '1':
            for address in addresses:
                address[key] = '1'
    
        elif val == 'X':
            newAddresses = []
            for address in addresses:
                for i in ['0', '1']:
                    address[key] = i
                    newAddresses.append(address[:])
            addresses = newAddresses
    
    for address in addresses:
        part2[int(''.join(address), 2)] = value
    

print(sum(part1.values()))
print(sum(part2.values()))
