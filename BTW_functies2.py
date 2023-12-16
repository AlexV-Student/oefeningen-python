
def korting(prijs, korting):
	prijs_met_korting = prijs - (prijs * (korting/100))
	return prijs_met_korting

def bedrag_met_btw(prijs):
	prijs_met_btw = prijs + (prijs * 0.21)
	return prijs_met_btw

if __name__ == '__main__':
	korting()
	bedrag_met_btw()