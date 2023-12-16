import BTW_functies2

bedrag = float(input('Bedrag: '))
korting = float(input('Kortingspercentage: '))

bedrag_met_korting = BTW_functies2.korting(bedrag, korting)
bedrag_met_korting_en_btw = BTW_functies2.bedrag_met_btw(bedrag_met_korting)

print('Het bedrag inclusief korting en btw bedraagt ', bedrag_met_korting_en_btw)