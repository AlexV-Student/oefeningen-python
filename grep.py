given_file = input('Voer het pad in voor het bestand waarin je wenst te zoeken: \n')
given_string = input('Voer het element in dat je wenst te zoeken binnen het bestand: \n')

try:
	with open (given_file, 'r') as file:
		file_string = file.read()
		waar_gevonden = file_string.find(given_string)
		print(f'De gezochte string werd gevonden op positie {waar_gevonden}')


except Exception as e:
	print(f'Er is een fout opgetreden:\n {e}')