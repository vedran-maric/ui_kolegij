#2. Napisati Python funkciju koja filtrira vrijednosti rjecnika na osnovu visine i kao rezultat
# daje novi rjecnik. Argumenti funkcije trebaju biti rjecnik, i visina po kojoj se filtrira.
# (primjer: filtrira sve osobe koje su vece od odredene visine)
# Rjecnik:
# {'Pero Peric': 175, 'Marko Markic': 180, 'Jure Juric': 165, 'Marija Maric': 190}


def filtriraj_po_visini(rjecnik, granica):
    novi_rjecnik = {}

    # prolazimo kroz originalni rjecnik
    for ime, visina in rjecnik.items():
        if visina > granica:
            # ako je osoba visa od granice, spremamo ju u novi rjecnik
            novi_rjecnik[ime] = visina
    return novi_rjecnik




osobe = {'Pero Peric': 175, 'Marko Markic': 180, 'Jure Juric': 165, 'Marija Maric': 190}
print(filtriraj_po_visini(osobe, 180))
