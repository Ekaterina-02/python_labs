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

