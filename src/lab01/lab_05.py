fio=input('Введите ФИО: ').split()
length=len(fio[0] + fio[1] + fio[2]) + 2
inicial=[fio[0][0].upper(),fio[1][0].upper(),fio[2][0].upper()]
inicial=''.join(inicial)
print(f'Инициалы: {inicial}.')
print(f'Длина (символов): {length}')