from abc import ABC

# abstracte superklasse Dier
class Dier(ABC):
    def __init__(self, naam, aantal_poten):
        # alle attributen als protected
        self._naam = naam
        self._poten = aantal_poten
        self._huid = None   # None want niet bepaald in superklasse
        self._geluid = None # None want niet bepaald in superklasse

    def geef_naam(self):
        return self._naam

    def geef_aantal_poten(self):
        return self._poten

    def maak_geluid(self):  # deze methode hoeft enkel in superklasse aanwezig te zijn
        return self._geluid

    def geef_huid(self):
        print("De huid van", self._naam, "bestaat uit", self._huid)


# 6 subklassen die overerven van de klasse Dier
class Vis(Dier):
    # Klasse die een vis voorstelt
    def __init__(self, naam):
        super().__init__(naam, 0)  # aantal poten is altijd nul bij een vis
        self._huid = "schubben"
    
class Reptiel(Dier):
    # Klasse die een reptiel voorstelt
    def __init__(self, naam, poten):
        super().__init__(naam, poten)
        self._huid = "schubben"
    
class Zoogdier(Dier):
    # Klasse die een zoogdier voorstelt
    def __init__(self, naam, poten):
        super().__init__(naam, poten)
        self._huid = "lederhuid"

class Vogel(Dier):
    # Klasse die een vogel voorstelt
    def __init__(self, naam):
        super().__init__(naam, 2)  # aantal poten is altijd 2 bij een vogel
        self._huid = "veren"

class Insect(Dier):
    # Klasse die een insect voorstelt
    def __init__(self, naam):
        super().__init__(naam, 6)  # aantal poten is altijd 6 bij een insect
        self._huid = 'exoskelet'

class Amfibie(Dier):
    # Klasse die een amfibie voorstelt
    def __init__(self, naam, poten):
        super().__init__(naam, poten)
        self._huid = "slijmhuid."  


# Subklassen van specifieke diersoorten
class Kat(Zoogdier):
    # Klasse die een kat voorstelt
    def __init__(self, naam):
        super().__init__(naam, 4)
        self._geluid = "miauw"  

class Hond(Zoogdier):
    # Klasse die een hond voorstelt
    def __init__(self, naam):
        super().__init__(naam, 4)
        self._geluid = "blaf"  

class Kikker(Amfibie):
    # Klasse die een kikker voorstelt
    def __init__(self, naam):
        super().__init__(naam, 4)
        self._geluid = "kwaak"

class Roodborstje(Vogel):
    # Klasse die een roodborstje voorstelt
    def __init__(self, naam):
        super().__init__(naam)
        self._geluid = "tjielp" 

class Clownvis(Vis):
    # Klasse die een clownvis voorstelt
    def __init__(self, naam):
        super().__init__(naam)
        self._geluid = "blub" 

class Muis(Zoogdier):
    # Klasse die een muis voorstelt
    def __init__(self, naam):
        super().__init__(naam, 4)
        self._geluid = "piep"
    

# Maak de objecten van de dieren aan
# deze keer gebruik makend van een list
dieren = []
dieren.append(Clownvis("Nemo"))
dieren.append(Hond("Fluffy"))
dieren.append(Kat("Tom"))
dieren.append(Muis("Jerry"))
dieren.append(Kikker("Pipa"))
dieren.append(Roodborstje("Jeremy"))

# Print de naam, het aantal poten en het geluid
# en print het huidtype van alle dieren
for dier in dieren:
    print(dier.geef_naam(), "heeft", dier.geef_aantal_poten(), "poten en zegt", dier.maak_geluid())
    dier.geef_huid()
    print()