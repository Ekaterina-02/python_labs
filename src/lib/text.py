### A номер
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
# text - обязательный параметр (строка для обработки)
# casefold, yo2e - опциональные параметры
# -> str - функция возвращает строку
    if casefold==True:  # проверяем надо ли приводить к нижнему регистру
        text=text.casefold()
    if yo2e==True:  # проверяем надо ли заменять букву 'ё' на 'е'
        text=text.replace('ё', 'e')
    text=text.replace('\n', ' ').replace('\r', ' ').replace('\t', ' ')
    while '  ' in text:
        text=text.replace('  ', ' ') #удаляем двойные пробелы
    text=text.strip() # удаляем пробелов в начале и конце
    return text


def tokenize(text: str) -> list[str]:
    text_new=[]  # пустой список для хранения обработанных символов, работаем только с дефисами
    for i in range(len(text)):
        if text[i] == '-':
            if i > 0 and i < len(text) - 1:  # дефис не находится в начале или конце строки
                if (text[i-1].isalnum() or text[i-1] == '_') and (text[i+1].isalnum() or text[i+1] == '_'):  # символы слева и справа от дефиса-буквы/цифры или подчеркивания
                    text_new.append('_') # временная замена дефиса
        else:
            text_new.append(text[i])
    text_new = ''.join(text_new)+' ' # преобразуем спиосок символов в строку и пробел, без него слово не добавится в результат
    word=''  # накопление текущего слова
    result=[] # хранение готовых слов
    for x in text_new:
        if x.isalnum() or x=='_':
            word+=x
        else:
            if len(word)!=0:
                word=word.replace('_', '-')
                result.append(word)
                word=''
    return result

def count_freq(tokens: list[str]) -> dict[str, int]:
    result={}  # пустой словарь, где хранится слова и их количество
    for i in tokens:
        result[i]=result.get(i, 0)+1 # ищет слово i в словаре result, если есть-возвращает количество, если нет-возвращает 0
    sorted_dict={}  # новый пустой словарь для отсортированных значений
    s=sorted(result.keys())  # cортируем все ключи из словаря по алфавиту
    for key in s:
        sorted_dict[key]=result[key] # сохраняем значение из исходного словаря в новый, под тем же ключом
    return sorted_dict


def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    spisoc=list(freq.items())  # преобразуем словарь в список кортежей (пар)
    sorted_letters=sorted(spisoc, key=lambda x: x[0]) # cортируем по алфавиту (по слову)
    sorted_counts=sorted(sorted_letters, key=lambda x: x[1], reverse=True) # cортируем список по количеству
    # при равенстве количеств сохраняется порядок из предыдущей сортировки (по алфавиту)
    sorted_counts_new=sorted_counts[:n]
    return sorted_counts_new