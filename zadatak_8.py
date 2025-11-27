#8. Za danu listu stringova, vrati rječnik čiji će ključevi biti znakovi iz stringova, a vrijednosti
#lista stringova koji sadrže taj znak po redoslijedu pojavljivanja u originalnom stringu.
#Napravite vlastitu funkciju,
#Npr. za listu ['dobar','dan'] će se dobiti rječnik
# {'d': ['dobar', 'dan'], 'o': ['dobar'],'b':['dobar'],'a':['dobar', 'dan'], 'r': ['dobar'], 'n': ['dan']}

def znakovi_u_stringovima(lst):
    result = {}
    for s in lst:
        for ch in s:
            result.setdefault(ch, [])
            if s not in result[ch]:
                result[ch].append(s)
    return result

print(znakovi_u_stringovima(['dobar', 'dan']))
