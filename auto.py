# een class Auto met attributen; merk, zitplaatsen, kmstand en ecoscore
class Auto:

	# Maak een lijst met passagiers waar alle methoden binnen de klasse toegang toe hebben. Deze lijst is een klassevariabele
	__passagiers = []

	# initialiseer een object van de class Auto
	def __init__(self, merk, zitplaatsen, kmstand, ecoscore):
		self.__merk = merk
		self.__zitplaatsen = zitplaatsen
		self.__kmstand = kmstand
		self.__ecoscore = ecoscore

	# een methode waarbij 1 of meerdere passagiers kunnen instappen, het aantal zitplaatsen wordt dan per passagier verminderd met 1 en weergegeven
	# de ingestapte passagiers worden aan de klassevariabele __passagiers toegevoegd
	def stap_in(self, passagiers):
		for passagier in passagiers:
			Auto.__passagiers.append(passagier)
			self.__zitplaatsen -= 1
		return self.__zitplaatsen

	# een methode waarbij 1 of meerdere passagiers kunnen uitstappen, het aantal zitplaatsen wordt dan per uitgestapte passagier vermeerderd met 1 en weergegeven
	# de uitgestapte passagiers worden uit de klassevariabele __passagiers verwijderd, zit een opgegeven passagier niet in de lijst dan wordt er een boodschap weergegeven
	def stap_uit(self, passagiers):
		for passagier in passagiers:
			if passagier in Auto.__passagiers:
				Auto.__passagiers.remove(passagier)
				self.__zitplaatsen += 1
			else:
				print(f'{passagier} is niet aan boord.')
		return self.__zitplaatsen

	# geef de inhoud van de klassevariabele __passagiers weer
	def geef_passagiers(self):
		return Auto.__passagiers

	# werk de kilometerstand bij door een aantal opgegeven kilometers op te tellen bij de originele opgegeven kilometerstand
	def update_kmstand(self, kms):
		self.__kmstand += kms
		return self.__kmstand

dikke_bmw = Auto('BMW', 5, 10000, 8)
print(dikke_bmw.stap_in(['Alexander', 'Justine']))
print(dikke_bmw.geef_passagiers())
print(dikke_bmw.stap_uit(['Alexander', 'Sebastien']))
print(dikke_bmw.update_kmstand(200))