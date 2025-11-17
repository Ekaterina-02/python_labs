### Лабораторная работа № 1
### 1 номер

```python
name=input('Введите имя: ')
age=int(input('Введите возраст: '))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```

![01_greeting](/images/lab01/Снимок%20экрана%202025-09-17%20165619.png)

### 2 номер

```python
a=float(input('Введите число: ').replace(',','.'))
b=float(input('Введите число: ').replace(',','.'))
print(f'sum={a+b}; avg={(a+b)/2:.2f}')
```

![02_sum_avg](/images/lab01/Снимок%20экрана%202025-09-17%20170604.png)

### 3 номер

```python
price, discount, vat=map(float,input('Введите цену, скидку, НДС: ').split())
base=price*(1-discount/100)
vat_amount=base*(vat/100)
total=base+vat_amount
print(f'База после скидки: {base:.2f}')
print(f'НДС: {vat_amount:.2f}')
print(f'Итого к оплате: {total:.2f}')
```

![03_discount_vat](/images/lab01/Снимок%20экрана%202025-09-17%20170853.png)

### 4 номер

```python
m=int(input('Введите минуты: '))
print(f'{(m//60)%24}:{m%60:02d}')
```

![04_minutes_to_hhmm](/images/lab01/Снимок%20экрана%202025-09-17%20173433.png)

### 5 номер

```python
fio=input('Введите ФИО: ').split()
length=len(fio[0] + fio[1] + fio[2]) + 2
inicial=[fio[0][0].upper(),fio[1][0].upper(),fio[2][0].upper()]
inicial=''.join(inicial)
print(f'Инициалы: {inicial}.')
print(f'Длина (символов): {length}')
```

![05_initials_and_len.py](/images/lab01/Снимок%20экрана%202025-09-22%20112140.png)



### Лабораторная работа № 2
### 1-A номер

```python
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums)==0:
        return ValueError
    return(min(nums),max(nums))
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))
```

![01-A_arrays.py](/images/lab02/Снимок%20экрана%202025-09-24%20155533.png)

### 1-B номер

```python
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    result=[]
    m=-10*10
    nums=sorted(nums)
    for i in nums:
        if i>m:
            result.append(i)
            m=i
    return result
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
```

![01-B_arrays.py](/images/lab02/Снимок%20экрана%202025-09-29%20214002.png)

### 1-C номер

```python
def flatten(mat: list[list | tuple]) -> list:
    for a in mat:
        if not(isinstance(a,(list,tuple))):
            return TypeError
    result=[]
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            result.append(mat[i][j])
    return result
print(flatten([[1, 2], [3, 4]]))
print(flatten(([1, 2], (3, 4, 5))))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
```

![01-C_arrays.py](/images/lab02/Снимок%20экрана%202025-09-29%20214215.png)

### 2-A номер

```python
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
```

![02-A_matrix.py](/images/lab02/Снимок%20экрана%202025-09-29%20214531.png)

### 2-B номер

```python
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
```

![02-B_matrix.py](/images/lab02/Снимок%20экрана%202025-09-29%20214820.png)

### 2-C номер

``` python
def col_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat)==0:
            return []
    for a in range(len(mat)):
        if len(mat[a])!=len(mat[0]):
            return ValueError
    sums=[]
    for j in range(len(mat[0])):
        s=0
        for i in range(len(mat)):
            s=s+mat[i][j]
        sums.append(s)
    return sums
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
```

![02-C_matrix.py](/images/lab02/Снимок%20экрана%202025-09-29%20215014.png)

### 3 номер

```python
def format_record(rec: tuple[str, str, float]) -> str:
    if len(rec)!=3:
        return ValueError
    if type(rec[0])!=str or type(rec[1])!=str:
        return ValueError
    if type(rec[2])!=float:
        return ValueError
    fio=rec[0].split()
    group=rec[1]
    gpa_new=rec[2]
    gpa=f'{gpa_new:.2f}'
    fio1=''
    f=0
    
    for i in range(len(fio)):
        if fio[i]!='' and f==0:
            first=fio[i][0].upper()
            fio1=first+fio[i][1:]
            f=1
        elif fio[i]!='' and f==1:
            first=fio[i][0].upper()
            fio1=fio1+' '+first+'.'
    result=f'{fio1},гр. {group}, GPA {gpa}'
    return result
print(format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)))
print(format_record(("Петров Пётр", "IKBO-12", 5.0)))
print(format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)))
print(format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999)))
```

![3_tuples.py](/images/lab02/Снимок%20экрана%202025-09-30%20233046.png)



### Лабораторная работа № 3
### A номер 1

```python
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
print(normalize("ПрИвЕт\nМИр\t"))
print(normalize("ёжик, Ёлка"))
print(normalize("Hello\r\nWorld"))
print(normalize("  двойные   пробелы  "))
```

![normalize](/images/lab03/Снимок%20экрана%202025-10-08%20225646.png)

### A номер 2

```python
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
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему круто"))
print(tokenize("2025 год"))
print(tokenize("emoji 😀 не слово"))
```

![tokenize](/images/lab03/Снимок%20экрана%202025-10-08%20225427.png)

### A номер 3

```python
def count_freq(tokens: list[str]) -> dict[str, int]:
    result={}  # пустой словарь, где хранится слова и их количество
    for i in tokens:
        result[i]=result.get(i, 0)+1 # ищет слово i в словаре result, если есть-возвращает количество, если нет-возвращает 0
    sorted_dict={}  # новый пустой словарь для отсортированных значений
    s=sorted(result.keys())  # cортируем все ключи из словаря по алфавиту
    for key in s:
        sorted_dict[key]=result[key] # сохраняем значение из исходного словаря в новый, под тем же ключом
    return sorted_dict
print(count_freq(["a","b","a","c","b","a"]))
print(count_freq(["привет", "мир", "привет"]))
```

![count](/images/lab03/Снимок%20экрана%202025-10-08%20225818.png)

### A номер 4

```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:
    spisoc=list(freq.items())  # преобразуем словарь в список кортежей (пар)
    sorted_letters=sorted(spisoc, key=lambda x: x[0]) # cортируем по алфавиту (по слову)
    sorted_counts=sorted(sorted_letters, key=lambda x: x[1], reverse=True) # cортируем список по количеству
    # при равенстве количеств сохраняется порядок из предыдущей сортировки (по алфавиту)
    sorted_counts_new=sorted_counts[:n]
    return sorted_counts_new
print(top_n({"bb": 2, "aa": 2, "cc": 1}))
print(top_n({"bb": 2, "aa": 2, "cc": 1}, n=2))
```

![count](/images/lab03/Снимок%20экрана%202025-10-09%20000330.png)

### A номер 4

```python
### B номер 
import sys
from lib.text import normalize, tokenize, count_freq, top_n

def text_statistics():
    text_vvod=sys.stdin  # получаем объект для чтения ввода с клавиатуры
    text=text_vvod.read()  # читаем весь текст, который ввели до нажатия Ctrl+D
    if text=='':
        print('нет введенного текста')
        return
    normalize_text=normalize(text)
    tokenize_text=tokenize(normalize_text)
    count_freq_text=count_freq(tokenize_text)
    top_n_text=top_n(count_freq_text,5)
    print(f'Всего слов: {len(tokenize_text)}')
    print(f'Уникальных слов: {len(set(tokenize_text))}')
    print("Топ-5:")  # заголовок для списка самых частых слов
    for word, count in top_n_text:
        print(f"{word}:{count}")
if __name__ == "__main__":  # проверяем, запущен ли файл как основная программа
    text_statistics()
```
![text_statistics](/images/lab03/Снимок%20экрана%202025-10-24%20110912.png)



### Лабораторная работа № 4
### номер A.1

```python
from pathlib import Path # Импортируем класс Path из модуля pathlib для работы с путями файлов
def read_text(path: str | Path, encoding: str="utf-8") -> str:
    
    # path - строка или объект Path (путь к файлу)
    # encoding - кодировка файла, по умолчанию utf-8
    # -> str - функция возвращает строку (содержимое файла)
    
    p=Path(path) # Преобразуем переданный путь в объект Path для удобной работы
    if not p.exists(): # Проверка существования файла по указанному пути
        raise FileNotFoundError('Файл не найден')
    
        """
        Выбор другой кодировки:
        в кодировке по умолчанию (UTF-8):
        read_text("file.txt")
        в кодировке Windows-1251:
        read_text("file.txt", encoding="cp1251")
        в кодировке KOI8-R:
        read_text("file.txt", encoding="koi8-r")
        """
        
    return p.read_text(encoding=encoding)  # Читаем и возвращаем файл в указанной кодировке
```

![read_text](/images/lab04/Снимок%20экрана%202025-10-28%20112013.png)

### номер A.2

```python
import csv
from pathlib import Path   # Импортируем класс Path для работы с путями файлов
from typing import Iterable, Sequence   # Импортируем типы данных
# Iterable - означает "что-то, по чему можно пройтись циклом for"
# Sequence - означает "что-то упорядоченное, к элементам можно обращаться по индексу"

def write_csv(rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None) -> None:
"""
rows - данные для записи
path - путь к файлу (может быть строкой или объектом Path)
header - заголовок таблицы (кортеж строк или None, если заголовка нет)
-> None -не возвращает никакого значения
"""
    p = Path(path)
    rows = list(rows) # Содаем список для многоразового обращения к данным
    with p.open('w', newline='', encoding = 'utf-8') as f: 
    # 'w' - режим записи
    # newline='' - отключаем автоматическую обработку переносов строк
    # encoding='utf-8' - устанавливаем кодировку UTF-8
    # as f - создаем переменную f для работы с файлом
        w = csv.writer(f)  # Создаем объект writer для записи данных
        if header is not None:
            w.writerow(header)   # Записываем заголовок как первую строку в CSV файл
        if rows:
            for row in rows:
                if len(row) != len(rows[0]):
                    raise ValueError("Строки имеют разную длину!")
        for row in rows:
            w.writerow(row)   # Записываем текущую строку в CSV файл ничего не возвращая
```
![write_csv](/images/lab04/Снимок%20экрана%202025-10-28%20112306.png)

### номер B

```python
import sys
all_paths=sys.path  # Получаем список всех путей
all_paths.append('C:/Users/user/Desktop/python_labs/src')
from lib.text import normalize, tokenize, count_freq, top_n
from lib.io_txt_csv import read_text, write_csv

# read_text - функция для чтения текстовых файлов
# write_csv - функция для записи данных в CSV файлы

try:
    raw_text = read_text('data/lab04/input.txt') # Пытаемся прочитать файл 'data/lab04/input.txt'
except FileNotFoundError as e: # Если файл не найден, то инфа об ошибке пишется в e
    print(f"Ошибка: {e}")  # в f-строке - детали ошибки из переменной 'e'
    sys.exit(1) # Завершаем программу с кодом ошибки 1

raw_text=tokenize(normalize(raw_text))
word=count_freq(raw_text)
text_counts=top_n(word)
print('Всего слов:', len(raw_text))
print('Уникальных слов:', len(set(raw_text)))
print('Топ-5:')
for i in text_counts:  
    print( f'{i[0]}:{i[1]}') 
write_csv(text_counts, 'data/lab04/report.csv', ("word","count"))

# Записываем результаты анализа в CSV файл
# text_counts - список кортежей для записи
# 'data/lab04/report.csv' - путь к файлу
# ("word","count") - заголовок таблицы
```
![write_csv_B](/images/lab04/Снимок%20экрана%202025-10-28%20115302.png)
![write_csv_B](/images/lab04/Снимок%20экрана%202025-10-28%20230342.png)



### Лабораторная работа № 5
### номер 1

```python
from pathlib import Path
import json
import csv
from typing import Union
def json_to_csv(json_path: str | Path, csv_path: str | Path, encoding: str = "utf-8") -> None:
    json_path=Path(json_path)  # Преобразуем входной путь в объект Path

    if not json_path.exists():   # Проверяем существование JSON файла
        raise FileNotFoundError("Файл не найден")

    with json_path.open("r", encoding='utf-8') as json_file:
        
    # Открываем JSON файл для чтения
    # 'with' -  закрытие файла даже при ошибках
    # 'encoding=utf-8' - правильное чтение русских символов
    
        try:
            data_json = json.load(json_file) # Пытаемся прочитать и преобразовать JSON в Python объект
        except json.JSONDecodeError:
            raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not data_json or not isinstance(data_json, list): # Проверка что данные не пустые и являются списком
        raise ValueError("Пустой JSON или неподдерживаемая структура")

    for row in data_json:  # Проверка что каждый элемент в списке - словарь
        if not isinstance(row, dict):
            raise ValueError("JSON должен содержать список словарей")

    csv_path = Path(csv_path)  # Преобразуем выходной путь в объект Path
   
    with csv_path.open("w", newline="", encoding=encoding) as csv_file:
        # Открываем CSV файл для записи
        writer = csv.DictWriter(csv_file, fieldnames=tuple(data_json[0].keys()))
        # Создаем объект для записи CSV из словарей
        # fieldnames - сохраняет порядок и названия колонок
        # tuple() - преобразуем в кортеж для неизменяемости
        writer.writeheader() # Записываем заголовок таблицыу, использует fieldnames
        writer.writerows(data_json)
        # Записываем все данные из JSON в CSV
        # writerows() принимает список словарей и записывает каждый как строку CSV


from pathlib import Path
import json
import csv
import sys
def csv_to_json(csv_path: str | Path, json_path: str | Path, encoding: str = "utf-8") -> None:
    
    csv_path = Path(csv_path)  # Преобразуем входной путь CSV в объект Path
    if not csv_path.exists():  # Проверяем существование CSV файла по указанному пути
        raise FileNotFoundError('Файл не найден')

    with csv_path.open("r", encoding='utf-8') as csv_file:
    # Открываем CSV файл для чтения
    # 'with' -  закрытие файла даже при ошибках
    # 'encoding=utf-8' - правильное чтение русских символов
    
        read_csv = csv.DictReader(csv_file)
        # Создаем объект для чтения CSV файла, автоматически используя первую строку как заголовки
        # Преобразует каждую последующую строку в словарь с ключами (заголовков)
        
        if not read_csv.fieldnames:
            raise ValueError("CSV-файл не содержит заголовков или пуст")
        data_csv = []  # Создаем пустой список для хранения всех строк данных из CSV файла
        for row in read_csv:
            data_csv.append(row)  # Добавляем каждую строку, которая становится словарем в список            
    if not data_csv:  # Проверка на существование хотя бы одной строки данных в CSV
        raise ValueError("CSV-файл пуст")

    json_path = Path(json_path)   # Преобразуем выходной путь JSON в объект Path
    with json_path.open("w", encoding='utf-8') as json_file:
        json.dump(data_csv, json_file, ensure_ascii=False, indent=2)
        # Записываем данные из списка в JSON файл
        # Преобразуем Python объекты в JSON формат и записываем в файл
        # indent=2 - добавляет отступы для читаемого форматирования

json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
```
![csv_gson](/images/lab05/Снимок%20экрана%202025-11-04%20212232.png)
![csv_gson](/images/lab05/Снимок%20экрана%202025-11-04%20212320.png)
![csv_gson](/images/lab05/Снимок%20экрана%202025-11-04%20215939.png)
![csv_gson](/images/lab05/Снимок%20экрана%202025-11-04%20215756.png)

### номер 2

```python
from pathlib import Path
import csv
from openpyxl import Workbook # Для создания и работы с Excel файлами
def csv_to_xlsx(csv_path: str | Path, xlsx_path: str | Path, encoding: str = "utf-8") -> None:
   
    csv_path = Path(csv_path)
    if not csv_path.exists(): # Проверяем существование CSV файла по указанному пути
        raise FileNotFoundError('Файл не найден')

    wb = Workbook() # Создаем новую книгу (файл) с помощью класса Workbook
    ws = wb.active # Получаем текущий лист в созданной книге Excel
    ws.title = "Sheet1" # Устанавливаем название для активного листа
    
    with csv_path.open("r", encoding='utf-8') as csv_file:
    # Открываем CSV файл для чтения
    # 'with' -  закрытие файла даже при ошибках
    # 'encoding=utf-8' - правильное чтение русских символов
        reader = csv.DictReader(csv_file)
        # Создаем объект для чтения CSV файла, автоматически используя первую строку как заголовки
        # Преобразует каждую последующую строку в словарь с ключами (заголовков)

        if not reader.fieldnames:  # Проверяем, что CSV файл содержит заголовки
            raise ValueError("CSV без заголовков или пуст")
        ws.append(reader.fieldnames) # Добавляем заголовки как первую строку в Excel лист

        for row in reader:
            row_values = [] # Создаем пустой список для хранения всех значений из текущей строки CSV
            for field in reader.fieldnames: # Получаем значение из текущей строки для конкретной колонки
                value = row[field]
                row_values.append(value)
            ws.append(row_values) # Добавляем значения текущей строки как новую строку в Excel лист

    xlsx_path = Path(xlsx_path) # Преобразуем выходной путь Excel в объект Path
    wb.save(xlsx_path) # Сохраняем созданную книгу, все данные, которые мы добавили, записываются в файл
    
csv_to_xlsx("data\\samples\\people.csv","data\\out\\people.xlsx")
```
![csv_xlx](/images/lab05/Снимок%20экрана%202025-11-04%20212140.png)
![csv_xlx](/images/lab05/Снимок%20экрана%202025-11-04%20220758.png)



### Лабораторная работа № 6
### номер 1

```python
import argparse
import sys
from pathlib import Path
from src.lib.text import tokenize, count_freq, top_n
def main(): 
    parser = argparse.ArgumentParser(description="CLI-утилиты") # Создаем главный парсер аргументов
    subparsers = parser.add_subparsers(dest="command") # Создаем контейнер для подкоманд (cat и stats)
    
    cat_parser = subparsers.add_parser("cat", help="Вывести содержимое файла") # Создаем парсер для команды
    cat_parser.add_argument("--input", required=True, help="Путь к входному файлу") # Добавляем обязательный аргумент
    cat_parser.add_argument("--number", action="store_true", help="Нумеровать строки") # Добавляем опциональный флаг -n для нумерации строк

    stats_parser = subparsers.add_parser("stats", help="Частоты слов в тексте")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument("--top", type=int, default=5, help="Количество наиболее частых слов")
    if len(sys.argv) == 1:   # Проверка: на наличие аргументов при вводе
        parser.error("Необходимо указать команду")
        
    args = parser.parse_args()  # Парсим аргументы командной строки, переданные при запуске программы
    filepath = Path(args.input) # Преобразуем строку пути в объект Path

    if not filepath.exists(): 
        raise FileNotFoundError("Файл не найден")
    if args.command == "cat":  
        with filepath.open("r", encoding="utf-8") as f:
            line_number = 1 # Счетчик строк
            for line in f:  # Читаем файл построчно
                line = line.rstrip("\n")  # удаляем символ перевода строки 
                if args.number:  # Если нумерация введена, выводим строку с ее номером
                    print(f"{line_number}: {line}")
                    line_number += 1
                else:
                    print(line)
    elif args.command == "stats":
        with filepath.open("r", encoding="utf-8") as file:
            text_lines = file.readlines()
        full_text = "".join(text_lines)
        tokens = tokenize(text=full_text)
        freq = count_freq(tokens=tokens)
        top = top_n(freq=freq, n=args.top)
        for word, count in top:
            print(f"{word} - {count}")
if __name__ == "__main__":  # Точка входа в программу - код выполнится только при прямом запуске файла
    main()
```
![argparse](/images/lab06/Лаба_6_CAT.png)
![argparse](/images/lab06/Лаба_6_STARS.png)
![argparse](/images/lab06/Лаба_6_пустой.png)

### номер 2

```python
import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx

def main():
    parser = argparse.ArgumentParser(description="CLI-утилиты") # Создаем главный парсер аргументов
    subparsers = parser.add_subparsers(dest="command") # Создаем контейнер для подкоманд, выбранная команда сохраненится в args.command
    
    json2csv_parser = subparsers.add_parser("json2csv", help="Конвертировать JSON в CSV") # Создаем парсер для команды
    json2csv_parser.add_argument("--input", required=True, help="Путь к JSON-файлу") # Добавляем обязательный аргумент --input
    json2csv_parser.add_argument("--output", required=True, help="Путь для CSV-файла") # Добавляем обязательный аргумент --output

    csv2json_parser = subparsers.add_parser("csv2json", help="Конвертировать CSV в JSON")
    csv2json_parser.add_argument("--input", required=True, help="Путь к CSV-файлу")
    csv2json_parser.add_argument("--output", required=True, help="Путь для JSON-файла")

    csv2xlsx_parser = subparsers.add_parser("csv2xlsx", help="Конвертировать CSV в XLSX")
    csv2xlsx_parser.add_argument("--input", required=True, help="Путь к CSV-файлу")
    csv2xlsx_parser.add_argument("--output", required=True, help="Путь для XLSX-файла")

    args = parser.parse_args() # Парсим аргументы командной строки, переданные при запуске программы
    if args.command == "json2csv": # Проверяем, какую команду выбрали
        json_to_csv(json_path=args.input,csv_path=args.output)
        # передаем входной файл из аргумента --input, выходной файл из аргумента --output

    elif args.command == "csv2json":
        csv_to_json(csv_path=args.input, json_path=args.output)

    elif args.command == "csv2xlsx":
        csv_to_xlsx(csv_path=args.input, xlsx_path=args.output)

if __name__ == "__main__":  # Точка входа в программу - код выполнится только при прямом запуске файла
    main()
```
![argparse](/images/lab06/Лаба_6_3.1.png)
![argparse](/images/lab06/Лаба_6_3.2.png)
![argparse](/images/lab06/Лаба_6_3.3.png)
![argparse](/images/lab06/Лаб_6_таблица.png)



### Лабораторная работа № 7
### номер A

```python
import pytest
from lib.text import count_freq, normalize, tokenize, top_n
# Параметризованный тест для normalize(), позволяет запустить один тест много раз с разными данными
@pytest.mark.parametrize(
    "src,expected",
    [
        ("ПрИвЕт\nМИр\t", "привет мир"),
        ("ёжик, Ёлка", "ежик, елка"),
        ("Hello\r\nWorld", "hello world"),
        ("  двойные   пробелы  ", "двойные пробелы"),
    ],
)
def test_normalize(src, expected):  # параметры src и expected из параметризаци
    assert normalize(src) == expected

# Параметризованный тест для функции tokenize()
@pytest.mark.parametrize(
    "src,expected",
    [
        ("привет мир", ["привет", "мир"]),
        ("hello,world!!!", ["hello", "world"]),
        ("по-настоящему круто", ["по-настоящему", "круто"]),
        ("2025 год", ["2025", "год"]),
        ("emoji 😀 не слово", ["emoji", "не", "слово"]),
    ],
)

def test_tokenize(src, expected):  # Тестовая функция для проверки tokenize()
    assert tokenize(src) == expected
    
def test_count_and_top():  # Тест для проверки count_freq() и top_n()
    tokens = ["a","b","a","c","b","a"]
    freq = count_freq(tokens)  # подсчета частот каждого элемента
    assert freq == {"a":3, "b":2, "c":1}  # Проверяем что правильно посчитало частоты
    assert top_n(freq, 2) == [("a",3), ("b",2)]  # Проверяем что возвращает 2 самых частых элемента

def test_top_tie_breaker():
    freq = count_freq(["bb","aa","bb","aa","cc"])
    assert top_n(freq, 2) == [("aa",2), ("bb",2)]

def test_dop(): # Проверяет как обрабатывают пустые входные данные
    assert normalize("") == ""
    assert tokenize("") == []
    assert count_freq([]) == {}
    assert top_n({}, 5) == []

def test_top_dop():  # Тест когда запрашиваем больше элементов чем есть
    freq = {"a": 3, "b": 2}
    assert top_n(freq, 5) == [("a", 3), ("b", 2)]
```

### номер B

```python
import csv
import json
from pathlib import Path
import pytest
from src.lib.json_csv import csv_to_json, json_to_csv

def write_json(path: Path, obj):  # Функция для записи JSON файла
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")

def read_csv_rows(path: Path): # Функция для чтения CSV файла
    with path.open(encoding="utf-8") as f:
        return list(csv.DictReader(f)) # читает CSV и преобразует каждую строку в список словарей

def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"   # Создаем путь к исходному файлу во временной папке
    dst = tmp_path / "people.csv"  # Создаем путь к целевому файлу во временной папке
    data = [{"name": "Alice", "age": 22}, {"name": "Bob", "age": 25}] # Вводим тестовые данные
    write_json(src, data)   # Записываем тестовые данные в JSON файл

    json_to_csv(str(src), str(dst))
    rows = read_csv_rows(dst) # Читаем результат CSV файла
    assert len(rows) == 2
    assert set(rows[0]) >= {"name", "age"} # В первой строке должны быть хотя бы колонки "name" и "age" (может быть больше)

def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    src.write_text("name,age\nAlice,22\nBob,25\n", encoding="utf-8") # Создаем CSV файл с заголовком и двумя строками

    csv_to_json(str(src), str(dst))
    obj = json.loads(dst.read_text(encoding="utf-8"))
    assert isinstance(obj, list) and len(obj) == 2 # должен быть списком и содержать 2 элемента
    assert set(obj[0]) == {"name", "age"} # В первом элементе должны быть олько ключи "name" и "age"(не должно быть лишних)


def test_json_to_csv_empty_raises(tmp_path: Path):  # Проверка обработки пустого JSON файла
    src = tmp_path / "empty.json"
    src.write_text("[]", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(tmp_path / "out.csv"))


def test_csv_to_json_no_header_raises(tmp_path: Path):  # Проверка обработки CSV файла без заголовка
    src = tmp_path / "bad.csv"
    src.write_text("", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(str(src), str(tmp_path / "out.json"))


def test_missing_file_raises():  # Тест 5: Проверка обработки несуществующего файла
    with pytest.raises(FileNotFoundError):
        csv_to_json("nope.csv", "out.json")
```
![pytest](/images/lab07/Лаба_7_1.png)
![pytest](/images/lab07/Лаба_7_2.png)
![pytest](/images/lab07/Лаба_7_3.png)