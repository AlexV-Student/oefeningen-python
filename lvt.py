import sys, sqlite3

script, input, database, output = sys.argv

tracks = []

try:
  with open(input,'r') as inputbestand:
    tracks = inputbestand.readlines()
except:
  print("Fout bij inlezen inputbestand")
  sys.exit(-1)


query = """
SELECT tracks.Name, albums.Title, artists.Name
FROM tracks JOIN albums USING(AlbumId)
JOIN artists USING(ArtistId)
WHERE tracks.Name like ?;
"""

try:
  dbconnectie = sqlite3.connect(database)
except:
  print("Geen connectie met database mogelijk.")
  sys.exit(-1)

tracklist = ""


for track in tracks:
  try:
    trackinfo = []
    mijncursor = dbconnectie.cursor()
    mijncursor.execute(query, (track.strip(),))
    trackinfo = mijncursor.fetchall()
  except:
    print(f"query naar {track} mislukt.")

  if len(trackinfo) == 0:
    tracklist = tracklist + f"{track.strip()}: niet gevonden.\n"
  else:
    for trackinfo_item in trackinfo:
      tracklist = tracklist + f"{trackinfo_item[0]}, {trackinfo_item[1]}, {trackinfo_item[2]}\n"

try:
  with open(output, 'w') as outputbestand:
    outputbestand.write(tracklist)
except OSError as error:
  print("Er ging iets fout bij het wegschrijven van de output")
  print(error)
