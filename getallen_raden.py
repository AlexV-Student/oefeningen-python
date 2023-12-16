from random import randint

rdm_getallen = []

i = 0
while i < 3:
	rdm_getallen.append(randint(0,30))
	i += 1
print(rdm_getallen)

speler_getallen = []

i = 0
while i < 3: 
	speler_input = input('Geef een getal tussen 0 en 30 in: ')
	speler_getallen.append(int(speler_input))
	i += 1

aantal_juist = []

for getal in speler_getallen:
    if getal in rdm_getallen:
        aantal_juist.append(getal)
print(aantal_juist)

if len(aantal_juist) == 1:
	print('Je raadde één juist getal. Je wint 10 euro!')
elif len(aantal_juist) == 2:
	print('Je raadde twee juiste getallen. je wint 30 euro!')
elif len(aantal_juist) == 3:
	print('Je raadde alle drie de getallen correct. Je wint 90 euro!')
else:
	print('Helaas je raadde geen enkel getal juist, je wint geen prijs.')