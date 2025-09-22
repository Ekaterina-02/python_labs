fio=input('Введите ФИО: ')
length=len(fio.strip())
fio=fio.split()
inicial=[fio[0][0].upper(),fio[1][0].upper(),fio[2][0].upper()]
inicial=''.join(inicial)
print(f'Инициалы: {inicial}.')
print(f'Длина (символов): {length}')