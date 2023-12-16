import sys

# check of argument meegegeven is

if len(sys.argv) != 2:
	print('Geef de naam van het \'.txt\' bestand dat je wil omzetten naar een \'.hmtl\' bestand in als argument.')
	sys.exit(1)

script_naam = sys.argv[0]
bestand = sys.argv[1]

# read file
try:
	with open(bestand, 'r') as file:
		inhoud = file.read()
except FileNotFoundError:
	print(f'File {bestand} not found.')
	sys.exit(-1)

# omzetten naar html

html = inhoud.replace('\n', '<br>')

#replace extension

bestand = bestand.split('.')
bestand[-1] = 'html'
bestand = '.'.join(bestand)

# write to html file

try:
	with open(bestand, 'w') as html_file:
		html_file.write(html)
		sys.exit(0)
except OSError:
	print(f'Something went wrong writing to {bestand}...')
	sys.exit(-1)