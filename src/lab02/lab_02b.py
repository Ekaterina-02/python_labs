def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat)==0:
            return []
    for a in range(len(mat)):
        if len(mat[a])!=len(mat[0]):
            return ValueError
    sums=[]
    for i in range(len(mat)):
        sums.append(sum(mat[i]))
    return sums
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))