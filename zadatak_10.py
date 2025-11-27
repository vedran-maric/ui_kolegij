#10. Za danu listu stringova vrati broj stringova iz liste kojima je duljina >=3 i koji imaju barem
#dvije znamenke jednake prvoj znamenci.
#Npr. za listu ['abc', 'aba', 'cc', 'ijki'] će vratiti 2

def broj_stringova(lst):
    count = 0
    for s in lst:
        if len(s) >= 3:
            if s.count(s[0]) >= 2:
                count += 1
    return count

print(broj_stringova(['abc', 'aba', 'cc', 'ijki']))
