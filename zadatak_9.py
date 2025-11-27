#9. Za danu matricu stringova pronađi elemente koji nisu brojcani stringovi i vrati rječnik čiji
#će ključ biti njihovih pozicija, a vrijednost sam element. Pozicija je predstavljena kao
#uređeni par (x,y) gdje je x broj reda, a y broj stupca elementa koji nije broj. Napravite
#vlastitu funkciju.
#Napomena: prvi redak i prvi stupac imaju poziciju 0. Npr. za matricu
# 5 4 a 1
# c 3 12 b
# 7 9 0 d
#se dobiva {(0,2): 'a', (1,0): 'c', (1,3): 'b', (2,3): 'd'}


def nenumericki(mat):
    result = {}
    for i, row in enumerate(mat):
        for j, val in enumerate(row):
            if not val.isdigit():
                result[(i, j)] = val
    return result

matrica = [
    ["5", "4", "a", "1"],
    ["c", "3", "12", "b"],
    ["7", "9", "0", "d"]
]

print(nenumericki(matrica))
