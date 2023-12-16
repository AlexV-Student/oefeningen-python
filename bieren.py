import csv

# Open het CSV-bestand en lees het in
csv_file_path = "bieren.csv"

# Initializeer variabelen voor het grootste alcoholpercentage en bijbehorend bier
max_alcohol_percentage = 0.0
beer_with_max_alcohol = ""
brewery_of_max_alcohol_beer = ""

with open(csv_file_path, mode='r', newline='', encoding='utf-8') as file:
    csv_reader = csv.reader(file, delimiter=',')
    
    # Lees de header om de indexen van de relevante kolommen te vinden
    header = next(csv_reader)
    naam_index = header.index("NAAM")
    alcohol_index = header.index("ALCOHOL %")
    brouwerij_index = header.index("BROUWERIJ")
    
    # Loop door de rijen om het hoogste alcoholpercentage en bijbehorende informatie te vinden
    for row in csv_reader:
        try:
            alcohol_percentage = float(row[alcohol_index])
            if alcohol_percentage > max_alcohol_percentage:
                max_alcohol_percentage = alcohol_percentage
                beer_with_max_alcohol = row[naam_index]
                brewery_of_max_alcohol_beer = row[brouwerij_index]
        except ValueError:
            # Als conversie naar float mislukt, ga door naar de volgende rij
            continue

# Print de resultaten
if beer_with_max_alcohol:
    print(f"Het hoogste alcoholpercentage is {max_alcohol_percentage}%.")
    print(f"Dit is te vinden in het bier genaamd {beer_with_max_alcohol}.")
    print(f"Dit bier wordt gebrouwen in de brouwerij genaamd {brewery_of_max_alcohol_beer}.")
else:
    print("Geen geldige gegevens gevonden in het CSV-bestand.")
