#3. Napisi program i funkciju loto642 koja simulira loto 6/42.
#a. Funkcija izvlaci 6 brojeva te jedan dopunski broj preko generatora slučajnih
#brojeva. Funkcija vraća listu loto brojeva.
#b. Brojeve igrača možete unijeti prilikom inicijalizacije liste (ručno).
#c. Potrebno je odrediti ukupan broj pogodataka pri izvlačenju i ispisati na ekran.
#d. Odrediti sumu pogođenih, minimum i maksimalni pogođeni broj

import random

def loto642():
    brojevi = random.sample(range(1, 43), 7)  # 6 + dopunski
    return brojevi[:6], brojevi[6]

# unos igračevih brojeva
igrac = [int(broj) for broj in input("Unesi svojih 6 brojeva odvojenih sa ',' : ").split(",")]

izvuceni, dopunski = loto642()
print("Izvučeni brojevi:", izvuceni)
print("Dopunski broj:", dopunski)

pogodci = [broj for broj in igrac if broj in izvuceni or broj == dopunski]

print("Broj pogodaka:", len(pogodci))
if pogodci:
    print("Suma pogodaka:", sum(pogodci))
    print("Min pogođeni broj:", min(pogodci))
    print("Max pogođeni broj:", max(pogodci))
