# dictionary met als key de naam van een programma en als value een booleanse waarde om aan te geven of het open source is.
opensource = {'ArcGIS': False,
              'LibreOffice': True,
              'MS Office': False,
              'Matlab': False,
              'QGIS': True,
              'R': True}

# overloop alle programma's in de dict en print enkel de open source programma's uit.
for i in opensource:
    Open_or_Closed = opensource[i]
    if Open_or_Closed:
        print(i)

# alle open source programma's afdrukken a.d.h.v. de filter() en lambda functies
print(list(filter(lambda x: opensource[x], opensource)))
