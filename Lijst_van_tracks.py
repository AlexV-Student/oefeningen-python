import sqlite3, sys

script, input, database, output = sys.argv

#list object genaamd tracks aanmaken
tracks = []

# het inputbestand inlezen en de lijnen opslaan in de lijst tracks, als inputbestand niet gevonden is -> foutmelding
try:
	with open(input, 'r') as inputbestand:
		tracks = inputbestand.readlines()
except FileNotFoundEror as err:
	print(f'Error: {err}!')
	sys.exit(-1)

# een query definiëren
# uit tabel tracks het kolom Name, uit tabel albums kolom Title, uit tabel artists kolom Name selecteren
# Voeg de tabellen tracks, albums, en artists samen op basis van overeenkomstige waarden in de kolommen AlbumId en ArtistId
# Beperk de resultaten tot de rijen waarvan de waarde in de kolom "Name" van de "tracks" tabel overeenkomt met het opgegeven patroon
query = '''
SELECT tracks.Name, albums.Title, artists.Name
FROM tracks JOIN albums USING(AlbumId)
JOIN artists USING(ArtistId)
WHERE tracks.Name LIKE ?;
'''

# verbinding met de database maken, als niet gelukt -> foutmelding
try:
	dbconnectie = sqlite3.connect(database)
except Exception as err:
	print(err)
	sys.exit(-1)

# een string tracklist maken
tracklist = ''

# voor elke track in de lijst met tracks ingelezen uit het inputbestand
# een lijst trackinfo maken
# een cursor object maken
# definiëren wat de cursor moet doen; de query uitvoeren, placeholder vervangen door track
# lijst trackinfo opvullen met alle objecten die de cursor ophaalt
for track in tracks:
	try:
		trackinfo = []
		mijncursor = dbconnectie.cursor()
		mijncursor.execute(query, (track.strip(),))
		trackinfo = mijncursor.fetchall()
	except:
		print(f'Query naar {track} mislukt.')

	if len(trackinfo) == 0:
		tracklist = tracklist + f'{track.strip()} niet gevonden.\n'
	else:
		for trackinfo_item in trackinfo:
			tracklist = tracklist + f'{trackinfo_item[0]}, {trackinfo_item[1]}, {trackinfo_item[2]}\n'

try:
	with open(output, 'w') as outputbestand:
		outputbestand.write(tracklist)
except OSError as err:
	print('Er ging iets fout bij het wegschrijven van de output')
	print(err)