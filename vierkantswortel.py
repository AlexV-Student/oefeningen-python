import math

gebruiker_getal = input("Geef een getal waarvan je de vierkantswortel wil berekenen: \n")
try:
	gebruiker_getal = float(gebruiker_getal)
	result = math.sqrt(gebruiker_getal)
	print(result)
except ValueError:
	print("Error: voer een geldig getal in")
except Exception as e:
	print(f"Er is een fout opgetreden: {e}")
