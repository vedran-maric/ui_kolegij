#4. Kreirati listu prirodnih brojeva od 50 elemenata (koristiti random funkciju). Za danu
#listu prirodnih brojeva stvori rječnik u kojemu će se nalaziti frekvencija pojavljivanja
#određene brojčane znamenke u svim brojevima iz liste
#Npr. za [423, 54, 45] broj 4 se pojavljuje 3 puta, 2 - 1 put, 3 -1 put, itd
#Napomena: ključevi rječnika neka budu brojevi, a ne stringovi.

import random

lista = [random.randint(0, 1000) for i in range(50)] #stvaramo 50 random brojeva
ucestalost = {
    0: 0,
    1: 0,
    2: 0,
    3: 0,
    4: 0,
    5: 0,
    6: 0,
    7: 0,
    8: 0,
    9: 0,
}

for random_broj in lista:
    for znamenka in str(random_broj): #broj rastavljamo na znamenke
        a = int(znamenka)
        ucestalost[a] = ucestalost.get(a) + 1 #povećava brojac za 1

print("Lista:", lista)
print("Frekvencije:", ucestalost)
