listfruits = []

i = 0
while i < 5:
	fruit = input("Geef een fruitsoort in: \n")
	if fruit not in listfruits:
		listfruits.append(fruit)
		i += 1
	else:
		print('Deze fruitsoort zit al in de lijst. Geef een ander fruit in.')

print(listfruits)