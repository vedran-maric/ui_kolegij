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
