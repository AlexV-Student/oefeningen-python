import csv

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

with open('studenten.csv', 'w', newline = '') as tabel_studenten:
    csv_writer = csv.writer(tabel_studenten, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)

    csv_writer.writerow(header)

    for student in studenten:
        csv_writer.writerow(student)

