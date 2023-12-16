
# file inlezen
with open('logfile.txt', 'r') as f:
	lines = f.readlines()



# lijnen opsplitsen in datum, uur, proces, info
lines = [line.split(':.') for line in lines]
for i, line in enumerate(lines):
	if len(line) > 1:
		Tijd_Uur_Type_Tekst = line[0].strip().split(' ')
		lines[i] = {'Datum':Tijd_Uur_Type_Tekst[0], 'Uur':Tijd_Uur_Type_Tekst[1], 'Type':Tijd_Uur_Type_Tekst[2], 'Tekst':line[1].strip()}
	else:
		lines[i] = {'Datum':None, 'Uur':None, 'Type':'BLOCK', 'Tekst':line[0].strip()}

# Hoe laat werd de RSVP Agent opgestart?
uur_opstart = lines[1]['Uur']
datum_opstart = lines[1]['Datum']
print(f'De RSVP agent werd opgestart op {datum_opstart} om {uur_opstart}')

# Hoe laat werd de RSVP Agent afgesloten?
uur_afsluit = lines[-1]['Uur']
datum_afsluit = lines[-1]['Datum']
print(f'De RSVP agent werd afgesloten op {datum_afsluit} om {uur_afsluit}')

# Print alle lijnen uit die een EVENT bevatten.		
events = [line for line in lines if line['Type'].lower() == 'event']
for event in events:
	print(event['Datum'], event['Uur'], event['Type'], event['Tekst'])