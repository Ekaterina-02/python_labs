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

