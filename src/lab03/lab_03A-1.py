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