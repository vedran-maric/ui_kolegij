def znakovi_u_stringovima(lst):
    result = {}
    for s in lst:
        for ch in s:
            result.setdefault(ch, [])
            if s not in result[ch]:
                result[ch].append(s)
    return result

print(znakovi_u_stringovima(['dobar', 'dan']))
