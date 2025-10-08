def count_freq(tokens: list[str]) -> dict[str, int]:
    result={}
    for i in tokens:
        result[i]=result.get(i, 0)+1
    sorted_dict={}
    s=sorted(result.keys())
    for key in s:
        sorted_dict[key]=result[key]
    return sorted_dict
print(count_freq(["a","b","a","c","b","a"]))
print(count_freq(["привет", "мир", "привет"]))