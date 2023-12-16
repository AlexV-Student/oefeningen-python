import os
from os import path
import shutil

header = ["Voornaam", "Familienaam", "U-nummer", "Richting"]
studenten = [
              ["Guido", "van Rossum", "u0465", "SD"],
              ["Steve", "Jobs", "u0145", "SD"],
              ["John", "von Neumann", "u0421", "CYB"],
              ["Bill", "Gates", "u0260", "SD"],
              ["Linus", "Torvalds", "u0912", "SD"],
              ["Sundar", "Pichai", "u0123", "AI"],
              ["Larry", "Page", "u0456", "AI"],
              ["Robin", "Li", "u0613", "BIT"],
              ["Grace", "Hopper", "u0435", "SD"],
              ["Jeffrey", "Bezos", "u0885", "BIT"],
              ["Alan", "Turing", "u0102", "AI"],
              ["Mark", "Zuckerberg", "u0542", "CYB"],
              ["Charles", "Robins", "u0648", "CYB"],
              ["Adele", "Goldberg", "u0893", "SD"],
              ["Lawrence", "Ellison", "u0247", "BIT"],
              ["Ada", "Lovelace", "u0111", "AI"],
              ["George", "Boole", "u0234", "BIT"],
              ["Donald", "Trump", "u0478", "USA"]
            ]

os.chdir('/Users/alexandervermeire/documents/vives/Programming in Python/Studenten')

for student in studenten:
	voornaam, achternaam, unummer, specialisatie = student
	groep = 'unknown'

	if specialisatie in ['AI', 'BIT']:
		groep = 'AI_BIT'
	elif specialisatie in ['SD', 'CYB']:
		groep = 'CYB_SD'

	onderverdeling = 'even' if int(unummer[-1]) % 2 == 0 else 'oneven'

	pad = os.path.join(groep, onderverdeling, f'{achternaam}_{voornaam}_{unummer}')

	os.makedirs(pad, exist_ok=True)

	with open(f'{pad}/htmlbestand.html', 'w') as file:
		file.write(f'<p>Beste {voornaam} {achternaam}<br>Welkom in de cursus Python!</p>')


	print(f'Folder aangemaakt: {pad}')

os.chdir('/Users/alexandervermeire/documents/vives/Programming in Python')

dir, tail = path.split('./studenten')
shutil.make_archive('Studenten_zip', 'zip', root_dir='.', base_dir='Studenten')