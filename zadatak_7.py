#7. Za dani riječnik čiji su ključevi imena studenata, a vrijednosti ocjene. Vrijednosti trebaju
#biti u obliku ntorke. Potrebno je vratiti rječnik čiji će ključevi biti prosječna ocjena
#(zaokružena - koristiti round() funkciju),a vrijednosti sortirana lista studenata koji su
#dobili tu prosječnu ocjenu.
#Npr. u rječniku {'ivan': (3,2,4), 'marko': (5,5,4), 'ana': (2,3,4)}, 'ivan' ima ocjene 3, 2, 4 i
#prosječna ocjena je 3.0, 'marko' ima ocjene 5, 4 i prosječna ocjena je 4.0, 'ana' ima
#ocjene 2, 3, 4 i prosječna ocjena je 3.0.
# Izlazni rječnik će biti {3: ['ana', 'ivan'], 4: ['marko']} jer 'ivan' i 'ana' imaju prosjek 3.0, a
#'marko' prosjek 4

def prosjek_ocjena(rjecnik):
    rezultat = {}
    for ime, ocjene in rjecnik.items():
        prosjek = round(sum(ocjene) / len(ocjene))
        rezultat.setdefault(prosjek, []).append(ime)

    for key in rezultat:
        rezultat[key].sort()
    return rezultat

print(prosjek_ocjena({'ivan': (3,2,4), 'marko': (5,5,4), 'ana': (2,3,4)}))
