def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat) == 0:
        return []
    for a in range(len(mat)):
        if len(mat[a]) != len(mat[0]):
            return ValueError
    sums = []
    for j in range(len(mat[0])):
        s = 0
        for i in range(len(mat)):
            s = s + mat[i][j]
        sums.append(s)
    return sums


print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
