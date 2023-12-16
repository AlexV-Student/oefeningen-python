from random import randint

def computer_getallen():
	getallen = set()
	i = 0
	while i < 3:
		getal = randint(0,30)
		getallen.add(getal)
		i += 1
	print(getallen)
	return(getallen)

def user_getallen():
	gebruiker_getallen = set()
	i = 0
	while i < 5:
		getal = int(input('Geef een getal tussen 0 en 30: '))
		if getal in gebruiker_getallen:
			print('Je gaf dit getal reeds in, probeer een ander getal')
		else:
			gebruiker_getallen.add(getal)
			i += 1
	return(gebruiker_getallen)

def controle(gebruiker_getallen, getallen):
	juiste_getallen = set()
	for getal in gebruiker_getallen:
		if getal in getallen:
			juiste_getallen.add(getal)
	return juiste_getallen

if __name__ == '__main__':
	computer_getallen = computer_getallen()
	user_getallen = user_getallen()

	juiste_getallen = controle(computer_getallen, user_getallen)
	if len(juiste_getallen) == 1:
		print('Je wint 10 euro!')
	elif len(juiste_getallen) == 2:
		print('Je wint 30 euro!')
	elif len(juiste_getallen) == 3:
		print('Je wint 60 euro!')
	else:
		print('Je raadde helaas niets juist')
