from pathlib import Path
import csv
from openpyxl import Workbook
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