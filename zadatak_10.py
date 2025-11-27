def broj_stringova(lst):
    count = 0
    for s in lst:
        if len(s) >= 3:
            if s.count(s[0]) >= 2:
                count += 1
    return count

print(broj_stringova(['abc', 'aba', 'cc', 'ijki']))
