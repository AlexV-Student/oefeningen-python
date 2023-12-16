# Class rechthoek definieren
# initiator bevat twee attributen, hoogte en breedte
# self verwijst naar het object van de class Rechthoek dat aangemaakt wordt
class Rechthoek:
	def __init__(self, hoogte, breedte):
		self.__hoogte = hoogte
		self.__breedte = breedte

	# methode om de attributen, hoogte en breedte, te wijzigen
	def zet_dimensies(self, hoogte, breedte):
		self.__hoogte = hoogte
		self.__breedte = breedte

	#methode om de attributen, hoogte en breedte, weer te geven
	def geef_dimensies(self):
		return self.__hoogte, self.__breedte

	# methode om de omtrek van het object van de class Rechthoek weer te geven
	def geef_omtrek(self):
		return 2 * (self.__breedte + self.__hoogte)

	# methode om de oppervlakte van het object/de instantie van de class Rechthoek weer te geven
	def geef_oppervlakte(self):
		return self.__breedte * self.__hoogte

# maak een object rechthoek1 aan van de class Rechthoek
rechthoek1 = Rechthoek(25, 30)
print(rechthoek1.geef_dimensies())
print(rechthoek1.geef_omtrek())
print(rechthoek1.geef_oppervlakte())