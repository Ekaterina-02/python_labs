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
        json.dump(data_csv, json_file, indent=2)
        # Записываем данные из списка в JSON файл
        # Преобразуем Python объекты в JSON формат и записываем в файл
        # indent=2 - добавляет отступы для читаемого форматирования