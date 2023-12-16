def korting_berekenen(prijs, korting):
	korting = (korting / 100) * prijs
	prijs = prijs - korting
	return prijs

def bedrag_met_btw(prijs):
	btw = (21 / 100) * prijs
	prijs = prijs + btw
	return prijs

if __name__ == '__main__':
	bedrag_met_btw(korting())
