from BTW_functies import korting_berekenen, bedrag_met_btw

bedrag = float(input('Geef een bedrag in: \n'))
korting = float(input('Geef het kortingspercentage in: \n'))

print(f'het bedrag is gelijk aan {bedrag}, met de korting van {korting:.0f}% afgetrokken bedraagt het totaalbedrag:', korting_berekenen(bedrag, korting))
print('Het bedrag inlusief 21% btw is gelijk aan: ', bedrag_met_btw(bedrag))