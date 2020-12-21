with open('input-21.txt') as f:
  lines = [line.strip() for line in f]

allIngredients = []
allAllergens = {}

for line in lines:
	ingredient, allergens = line.split(' (contains ')

	allergens = allergens[:-1].split(', ')
	ingredient = ingredient.split()
	allIngredients += ingredient
	for allergen in allergens:
		if allergen not in allAllergens:
			allAllergens[allergen] = set(ingredient)
		else:
			allAllergens[allergen] &= set(ingredient)

setOfAllergens = set()
for allergens in allAllergens.values():
  for allergen in allergens:
	setOfAllergens.add(allergen)

acc = 0
for allergen in allIngredients:
	if allergen not in setOfAllergens:
		acc+=1

print(acc)

