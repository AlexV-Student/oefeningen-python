'''Schrijf een functie die een tuple omzet naar een string m.b.v. een for-lus.'''

def tuple_to_string(tuple, sep=''):
	sep = input('Geef een separator value in: ') # Laat de gebruiker toe om een scheidingsteken (Engels: separator) te  definiëren
	for element in tuple: 						 # elk element afzonderlijk moet omgezet worden naar een string
		s1 = str(element)
		print(s1, end = sep)
		print(type(s1))

tuple_to_string(tuple = ('d','i','t',' ', 'i', 's', ' ', 'e', 'e', 'n', ' ', 'tuple'))

