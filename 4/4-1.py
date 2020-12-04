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
	if ('cid' not in keys and len(keys) == 1):
		continue

	if len(keys) > 1:
		continue
	
	valids += 1

print valids
