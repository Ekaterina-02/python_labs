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