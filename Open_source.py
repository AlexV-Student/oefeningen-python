opensource = {'ArcGIS': False,
              'LibreOffice': True,
              'MS Office': False,
              'Matlab': False,
              'QGIS': True,
              'R': True}

for program, value in opensource.items(): # alle keys doorlopen en enkel deze afdrukken die als value True hebben.
    if value == True:
        print(program)

filtered_programs= filter(lambda item: item[1] == True, opensource.items()) # zelfde als hierboven, maar dan via filter() functie.

for program, value in filtered_programs:
    print(program)
