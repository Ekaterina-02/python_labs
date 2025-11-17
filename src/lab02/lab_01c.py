def flatten(mat: list[list | tuple]) -> list:
    for a in mat:
        if not (isinstance(a, (list, tuple))):
            return TypeError
    result = []
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            result.append(mat[i][j])
    return result


print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
