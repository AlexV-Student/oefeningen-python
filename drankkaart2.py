drankkaart = {'Jupiler', 'Duvel', 'Witte Wijn', 'Rode Wijn', 'Spa Bruis', 'Spa Plat', 'Cola', 'Fruitsap'}
bestelling1 = ['Jupiler', 'Jupiler', 'Jupiler', 'Jupiler', 'Duvel', 'Duvel']
bestelling2 = ['Jupiler', 'Jupiler', 'Duvel', 'Limonade', 'Witte Wijn', 'Ice Tea', 'Cola', 'Cola']

def kaart_controle(bestelling):
	if set(bestelling).issubset(drankkaart):
		print('De bestelling komt eraan!')
	else:
		print('De volgende dranken werden niet gevonden op de kaart.')
		print(','.join(set(bestelling).difference(drankkaart)))

if __name__ == '__main__':
	kaart_controle(bestelling1)
	kaart_controle(bestelling2)
	bestelling2[bestelling2.index('Ice Tea')] = 'C O N K'
	kaart_controle(bestelling2) 