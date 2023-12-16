import sys

script, bestand, woord = sys.argv

if len(sys.argv) != 3:
	print('Geef zowel een betandsnaam als een bepaald woord dat je wenst te vinden in dat bestand in.')

try:
	with open(bestand, 'r') as f:
		lines = f.readlines()
		for line in lines:
			if woord in line:
				print(line)
except FileNotFoundError:
	print(f'het bestand {bestand} kon niet gevonden worden.')
except OSError:
	print(f'{bestand} is geen bestand.')
