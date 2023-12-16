import os
import shutil

print(os.path.abspath(os.getcwd()))

try:
	os.mkdir('temp')
except FileExistsError as e:
	print(f'Error: {e}')

source = 'devops.txt'  # te kopiëren bestand
destination = './temp/devops.txt'
shutil.copy(source,destination)

os.chdir('/Users/alexandervermeire/documents/vives/Programming in Python/temp')

try:
	with open('leeg.txt', 'x') as file:
		file.close()
except FileExistsError as e:
	print(f'Error: {e}')

os.chdir('/Users/alexandervermeire/documents/vives/Programming in Python')

with os.scandir('/Users/alexandervermeire/documents/vives/Programming in Python/temp') as entries:
	for entry in entries:
		print(entry.name)

shutil.rmtree('temp')
