def transpose(mat: list[list[float | int]]) -> list[list]:
    if len(mat)==0:
            return []
    for a in range(len(mat)):
        if len(mat[a])!=len(mat[0]):
            return 'ValueError'
    strocs=len(mat)
    colons=len(mat[0])
    result=[]
    for i in range(colons):
        colons1=[0]*strocs
        result.append(colons1)
    for s in range(strocs):
        for e in range(colons):
            result[e][s]=mat[s][e]
    return result
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))