from abc import ABC

# abstracte superklasse Dier
class Dier(ABC):
	def __init__(self, naam, aantal_poten):
		self._naam = naam
		self._poten = aantal_poten
		self._huid = None
		self._geluid = None

	def geef_naam(self):
		return self._naam

	def geef_aantal_poten(self):
		return self._poten

	def maak_geluid(self):
		return self._geluid

	def geef_huid(self):
		print('de huid van de ', self._naam, ' bestaat uit ', self._huid)

# 6 subklassen die overerven van de klasse Dier
class Vis(Dier):
	def __init__(self, naam):
		super().__init__(naam, 0) # het aantal poten bij een vis is altijd gelijk aan 0
		self._huid = 'schubben'

class Reptiel(Dier):
	def __init__(self, naam, poten):
		super().__init__(naam, poten)
		self._huid = 'schubben'

class Zoogdier(Dier):
	def __init__(self, naam, poten):
		super().__init__(naam, poten)
		self._huid = 'vacht'

class Vogel(Dier):
	def __init__(self, naam):
		super().__init__(naam, 2)
		self._huid = 'veren'

class Insect(Dier):
	def __init__(self, naam):
		super().__init__(naam, 6)
		self._huid = 'exoskelet'

class Amfibie(Dier):
	def __init__(self, naam, poten):
		super().__init__(naam, poten)
		self._huid = 'slijmhuid'

# Subklassen van specifieke diersoorten
class Kat(Zoogdier):
	def __init__(self, naam):
		super().__init__(naam, 4)
		self._geluid = 'miauw'

class Hond(Zoogdier):
    # Klasse die een hond voorstelt
    def __init__(self, naam):
        super().__init__(naam, 4)
        self._geluid = 'blaf'  

class Kikker(Amfibie):
    # Klasse die een kikker voorstelt
    def __init__(self, naam):
        super().__init__(naam, 4)
        self._geluid = 'kwaak'

class Roodborstje(Vogel):
    # Klasse die een roodborstje voorstelt
    def __init__(self, naam):
        super().__init__(naam)
        self._geluid = 'tjielp' 

class Clownvis(Vis):
    # Klasse die een clownvis voorstelt
    def __init__(self, naam):
        super().__init__(naam)
        self._geluid = 'blub' 

class Muis(Zoogdier):
    # Klasse die een muis voorstelt
    def __init__(self, naam):
        super().__init__(naam, 4)
        self._geluid = 'piep'
    

# Maak de objecten van de dieren aan
# deze keer gebruik makend van een list
dieren = []
dieren.append(Clownvis('Nemo'))
dieren.append(Hond('Fluffy'))
dieren.append(Kat('Tom'))
dieren.append(Muis('Jerry'))
dieren.append(Kikker('Pipa'))
dieren.append(Roodborstje('Jeremy'))

# Print de naam, het aantal poten en het geluid
# en print het huidtype van alle dieren
for dier in dieren:
    print(dier.geef_naam(), 'heeft', dier.geef_aantal_poten(), 'poten en zegt', dier.maak_geluid())
    dier.geef_huid()
    print()