'''Definieer een variabele "drankkaart" en ken er een set aan toe met de volgende dranken:
Jupiler, Duvel, Witte Wijn, Rode Wijn, Spa Bruis, Spa Plat, Cola, Fruitsap.
Definieer een variabele "bestelling1" die een list bevat met volgende bestelde dranken: 4 Jupiler, 2 Duvel
Definieer een variabele "bestelling2" die een list bevat met volgende dranken: 2 Jupiler, 1 Duvel, 1 Limonade, 1 Witte Wijn, 1 Ice Tea, 2 Cola'''

drankkaart = {'Jupiler', 'Duvel', 'Witte Wijn', 'Rode Wijn', 'Spa Bruis', 'Spa Plat', 'Cola', 'Fruitsap'}

bestelling1 = ['Jupiler', 'Jupiler', 'Jupiler', 'Jupiler', 'Duvel', 'Duvel']

bestelling2 = ['Jupiler', 'Jupiler', 'Duvel', 'Limonade', 'Witte Wijn', 'Ice Tea', 'Cola', 'Cola'] # 2 Jupiler, 1 Duvel, 1 Limonade, 1 Witte Wijn, 1 Ice Tea, 2 Cola

'''Definieer een functie die nagaat of alle bestelde dranken op de drankkaart staan. Om deze check uit te voeren mag je geen lus gebruiken! 
 Als alle dranken op de kaart staan, laat je de functie "Bestelling komt  eraan!" printen. Anders toont de functie een boodschap die aangeeft
 welke dranken niet op de kaart staan. Pas de bestelling aan door de dranken die niet op de kaart staan te vervangen. Probeer ook hier geen lussen te gebruiken!'''

def controle_kaart(drank=[]):
	if set(drank).issubset(drankkaart):
		print('Bestelling opgenomen')
	else:
		niet_op_kaart = set(drank) - drankkaart
		print('Eén of meerdere van deze dranken hebben wij niet op voorraad: \n ', niet_op_kaart)

controle_kaart(bestelling1)
controle_kaart(bestelling2)
