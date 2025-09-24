def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums)==0:
        return 'ValueError'
    return(min(nums),max(nums))
print(min_max([3, -1, 5, 5, 0]))
print([42])
print([-5, -2, -9])
print(min_max([]))
print([1.5, 2, 2.0, -3.1])