import re

passports = []
with open('input-4.txt') as f:
	rows = lines = f.readlines()
	rawPassportData = ""
	for row in rows:
		line = row.strip()
		isLastLine = row == rows[-1]

		if line == '' or isLastLine:
			
			if isLastLine:
				rawPassportData += " %s"%line

			keyValuePairs = rawPassportData.strip().split(' ')
			passport = {}

			for keyValuePair in keyValuePairs:
				key, value = keyValuePair.split(':')
				passport[key] = value

			passports.append(passport)
			rawPassportData = ''
			continue
		
		rawPassportData += " %s"%line

valids = 0

requiredKeys = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid'}
for passport in passports:
	keys = requiredKeys - set(passport.keys())
	
	if len(keys) > 1:
		continue

	if ('cid' not in keys and len(keys) == 1):
		continue

	if not (int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002):
		continue

	if not (int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020):
		continue

	if not (int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030):
		continue

	if not (passport['hgt'].find('cm') !=  -1) ^ (passport['hgt'].find('in') != -1):
		continue
	
	currentHeight = int(re.findall(r'\d+',passport['hgt'])[0])
	
	if (passport['hgt'].find('cm') > 0 and not (currentHeight >= 150 and currentHeight <= 193)):
		continue

	if (passport['hgt'].find('in') > 0 and not (currentHeight >= 59 and currentHeight <= 76)):
		continue
	
	if not passport['ecl'] in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'}:
		continue

	if not re.match(r'^#[a-zA-Z0-9]{6,6}$', passport['hcl']):
		continue

	if not re.match(r'^\d{9,9}$', passport['pid']):
		continue

	valids += 1

print 'Valid passports: %d'%valids
