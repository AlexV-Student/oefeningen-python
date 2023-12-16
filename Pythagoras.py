import math

def pythagoras(a, b, c=0):
	c = math.sqrt(math.pow(a, 2) + math.pow(b, 2))
	print(f'{c:.2f}')

if __name__ == '__main__':
	pythagoras(5, 5)