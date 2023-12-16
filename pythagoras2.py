import math

# functie die A**2 + B**2 = C**2 berekent. Voer de berekeningen uit door gebruik te  maken van de functies pow() en sqrt() uit de math module.

def pythagoras(a=0, b=0):
	c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
	print(f'{c:.2f}')

if __name__ == '__main__':
	pythagoras(20,20)
