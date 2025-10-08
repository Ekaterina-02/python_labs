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