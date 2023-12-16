'''
devops.txt
Lees de file "devops.txt" in en print de inhoud van de file uit. 
Hou rekening met eventuele fouten die kunnen optreden bij het openen of lezen van de file zodat je programma niet crasht en daarbij onduidelijke foutboodschappen geeft.
'''

try:
	with open('devops.txt', 'r') as file:
		lines = file.readlines()
		print(str(lines).strip('[]'))

except:
	print('mislukt')
