def euro_to_dollar(euro,bedrag_in_dollar=0):
	wisselkoers = float(input("Voer de huidige wisselkoers voor euro naar dollar in: \n"))
	if wisselkoers == "":
		wisselkoers = 1.12
	bedrag_in_dollar = euro * wisselkoers
	return(bedrag_in_dollar)

def dollar_to_euro(dollar, bedrag_in_euro=0):
	wisselkoers = float(input("Voer de huidige wisselkoers voor dollar naar euro in: \n"))
	if wisselkoers == "":
		wisselkoers = 1.12
	bedrag_in_dollar = dollar / wisselkoers
	return(bedrag_in_dollar)

def print_euro_to_dollar():
	euro = 50
	print(f'€{euro:.2f} is gelijk aan ${euro_to_dollar(euro):.2f}')

def print_dollar_to_euro():
	dollar = 100
	print(f'${dollar:.2f} is gelijk aan €{dollar_to_euro(dollar):.2f}')

if __name__ == '__main__':
	print_euro_to_dollar()
	print_dollar_to_euro()
