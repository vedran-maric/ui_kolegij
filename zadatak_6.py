#6. Postaviti parametre kružnice (r i koordinate središta (a, i b). Zatim je potrebno učitavati
#10 točaka koordinatnog sustava (realni brojevi).
# Za učitane točke provjeriti nalaze li se na kružnici. (25 bodova)
# Nakon što se učita točka (0, 0), ispisati koliki je omjer pogodaka kružnice ((broj
#točaka na kružnici)/(ukupni broj točaka)) u postotku (25 bodova)
#Formula kružnice : (x-a)2+(y-b)2=r2

import math

r = float(input("Polumjer r = "))
a = float(input("središte kružnice x = "))
b = float(input("središte kružnice y = "))

pogodci = 0
ukupno = 0

while ukupno < 10:
    x = float(input("Unesi x za " + str(ukupno+1) + ". točku: "))
    y = float(input("Unesi y za " + str(ukupno+1) + ". točku: "))

    if x == 0 and y == 0: #gasi program i ispisuje omjer
        break

    ukupno += 1
    if abs((x - a)**2 + (y - b)**2 - r**2): ##ako je na kruznici povecaj brojac
        pogodci += 1

print("Omjer pogodaka:", (pogodci / ukupno) * 100, "%")
