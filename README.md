### 1 номер

```
name=input('Введите имя: ')
age=int(input('Введите возраст: '))
print(f'Привет, {name}! Через год тебе будет {age+1}.')
```

![01_greeting](/images/Снимок%20экрана%202025-09-17%20165619.png)

### 2 номер

```
a=float(input('Введите число: ').replace(',','.'))
b=float(input('Введите число: ').replace(',','.'))
print(f'sum={a+b}; avg={(a+b)/2:.2f}')
```

![02_sum_avg](/images/Снимок%20экрана%202025-09-17%20170604.png)

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

![03_discount_vat](/images/Снимок%20экрана%202025-09-17%20170853.png)