### Лабораторная работа № 1
### 1 номер

```
name=input('Введите имя: ')
age=int(input('Введите возраст: '))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```

![01_greeting](/images/lab01/Снимок%20экрана%202025-09-17%20165619.png)

### 2 номер

```
a=float(input('Введите число: ').replace(',','.'))
b=float(input('Введите число: ').replace(',','.'))
print(f'sum={a+b}; avg={(a+b)/2:.2f}')
```

![02_sum_avg](/images/lab01/Снимок%20экрана%202025-09-17%20170604.png)

### 3 номер

```
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

```
m=int(input('Введите минуты: '))
print(f'{(m//60)%24}:{m%60:02d}')
```

![04_minutes_to_hhmm](/images/lab01/Снимок%20экрана%202025-09-17%20173433.png)

### 5 номер

```
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

```
def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums)==0:
        return 'ValueError'
    return(min(nums),max(nums))
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([]))
print(min_max([1.5, 2, 2.0, -3.1]))
```

![01-A_arrays.py](/images/lab02/Снимок%20экрана%202025-09-24%20155533.png)

### 1-B номер

```
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

```
def flatten(mat: list[list | tuple]) -> list:
    for a in mat:
        if not(isinstance(a,(list,tuple))):
            return 'TypeError'
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

```
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

```
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if len(mat)==0:
            return []
    for a in range(len(mat)):
        if len(mat[a])!=len(mat[0]):
            return 'ValueError'
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
            return 'ValueError'
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

```
def format_record(rec: tuple[str, str, float]) -> str:
    for i in rec:
        if str(i)=='':
            return 'ValueError'
    fio=str(rec[0]).split()
    group=str(rec[1])
    gpa_new=float(rec[2])
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