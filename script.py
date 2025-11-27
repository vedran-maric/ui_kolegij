import random
from collections import Counter

#1. Napisi program koji ispisuje cjelobrojne elemente koji se pojavljuju 3 ili vise puta unutar liste.
# Generiraj listu od 100 elemenata u rasponu vrijednosti od 0 do 30.

lista = [random.randint(0, 30) for i in range(100)] #generiranje liste
print("Lista:", lista)

brojac = Counter(lista) #broji koliko puta se koji broj ponovio
cesti_brojevi = [broj for broj, puta_ponovljen in brojac.items() if puta_ponovljen >= 3] # ubacuje broj za svaku
# iteraciju kada prebroji brojac.items() koji vraca uređen par koji razdvojimo u broj i puta_ponovljen

print("3 ili vise puta se priakzuju sljedeći brojevi:", cesti_brojevi)
