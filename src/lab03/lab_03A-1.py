def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold==True:
        text=text.casefold()
    if yo2e==True:
        text=text.replace('ё', 'e')
    text=text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    while '  ' in text:
        text=text.replace('  ', ' ')
    text=text.strip()
    return text
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))


def tokenize(text: str) -> list[str]:
    text_new=[]
    for i in range(len(text)):
        if text[i] == '-':
            if i > 0 and i < len(text) - 1:
                if (text[i-1].isalnum() or text[i-1] == '_') and (text[i+1].isalnum() or text[i+1] == '_'): 
                    text_new.append('_')
        else:
            text_new.append(text[i])
    text_new = ''.join(text_new)+' '
    word=''
    result=[]
    for x in text_new:
        if x.isalnum() or x=='_':
            word+=x
        else:
            if len(word)!=0:
                word=word.replace('_', '-')
                result.append(word)
                word=''
    return result
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))

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

def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    spisoc=list(freq.items()) 
    sorted_spisoc=sorted(spisoc, key=lambda x: x[1], reverse=True)
    return sorted_spisoc[:n]
print(top_n({"bb": 2, "aa": 2, "cc": 1}))
print(top_n({"bb": 2, "aa": 2, "cc": 1}, n=2))