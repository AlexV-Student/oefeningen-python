import sys

if len(sys.argv) -1 != 2:
	print("Je moet twee argumenten geven, de lengte en de breedte.")
	sys.exit(1)

script_naam = sys.argv[0]
lengte = sys.argv[1]
breedte= sys.argv[2]

if lengte.isnumeric() and breedte.isnumeric():
	if int(lengte) >=0 and int(breedte) >=0:
		oppervalekte = int(lengte) * int(breedte)
		print(f'De oppervlakte is: {oppervalekte}')
	else:
		print('Lengte en breedte moeten groter dan 0 zijn.')
else:
	print('Er is een fout opgetreden. Zorg ervoor dat je argumenten gehele getallen zijn.')
	