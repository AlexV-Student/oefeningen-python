import sys

if len(sys.argv) !=3:
	print('Geef zowel een bronbestand als een bestemmingsbestandsnaam in.')
	sys.exit(1)

source_file = sys.argv[1]
destination_file = sys.argv[2]

try:
	with open(source_file, 'r') as file:
		inhoud = file.read()

	with open (destination_file, 'w') as second_file:
		second_file.write(inhoud)
except Exception as err:
	print(f'Unexpected {err}, {type(err)}')
	raise

