'''
Vierkantswortel

Schrijf een progamma dat aan de gebruiker een getal vraagt en de  vierkantswortel van dat getal uitprint. 
Hou er rekening mee dat de  gebruiker foute input kan opgeven. 
Zorg dat in dat geval het programma  niet crasht en de gebruiker een duidelijke boodschap krijgt.
'''

import math

usernum = input("Geef een getal waarvan je graag de vierkantswortel wilt berekenen: \n")
try:
	result = math.sqrt(float(usernum))
	print(result)
except:
	print("Je gaf een ongeldige waarde op, probeer het opnieuw")

