def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    spisoc=list(freq.items()) 
    sorted_spisoc=sorted(spisoc, key=lambda x: x[1], reverse=True)
    return sorted_spisoc[:n]
print(top_n({"bb": 2, "aa": 2, "cc": 1}))
print(top_n({"bb": 2, "aa": 2, "cc": 1}, n=2))
