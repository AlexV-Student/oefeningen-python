import csv

with open('bieren.csv', 'r', newline='') as bieren:
	myReader = csv.reader(bieren, delimiter=',')
	header = next(myReader)
	table = [row for row in myReader]

col_bier = header.index('NAAM')
col_perc = header.index('ALCOHOL %')
col_brouw = header.index('BROUWERIJ')

max_perc = 0
max_bier = ''
max_brouw = ''

for row in table:
	perc = float(row[col_perc])
	if perc > max_perc:
		max_perc = perc
		max_bier = row[col_bier]
		max_brouw = row[col_brouw]

print(f'{max_bier} van brouwerij {max_brouw} bevat met {max_perc:.2f}% het meeste alchol.')
		