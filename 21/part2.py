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

allAllergens = {a : list(ingredient) for a, ingredient in allAllergens.items()}

while any(True for ingredient in allAllergens.values() if isinstance(ingredient, list) and len(ingredient) > 1):
	for allergen, ingredient in allAllergens.items():
		if isinstance(ingredient, list) and len(ingredient) == 1:
			allAllergens[allergen] = ingredient[0]
			for a, ing in allAllergens.items():
				if isinstance(ing, list) and ingredient[0] in ing:
					ing.remove(ingredient[0])

sortedAllergen = list(allAllergens.keys())
sortedAllergen.sort()

listOfIngredients = []
for allergen in sortedAllergen:
  listOfIngredients.append(allAllergens[allergen])

print ",".join(listOfIngredients)

