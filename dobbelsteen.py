from random import randint

# een class dobbelsteen die een waarde tussen 1 en 6 kan weergeven
class Dobbelsteen:
	__waarde = 0

	def __init__(self):
		pass
	# een methode werp die een willekeurig getal tussen 1 en 6 weergeeft
	def werp(self):
		self.__waarde = randint(1,6)
		return self.__waarde

# een instantie van de klasse dobbelsteen, er worden tien worpen gesimuleerd
dobbelsteen1 = Dobbelsteen()
for i in range(10):
	print(f'Worp {i + 1}	- ', dobbelsteen1.werp())