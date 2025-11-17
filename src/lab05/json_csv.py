from pathlib import Path
import json
import csv
from typing import Union


def json_to_csv(
    json_path: str | Path, csv_path: str | Path, encoding: str = "utf-8"
) -> None:
    json_path = Path(json_path)  # Преобразуем входной путь в объект Path

    if not json_path.exists():  # Проверяем существование JSON файла
        raise FileNotFoundError("Файл не найден")

    with json_path.open("r", encoding="utf-8") as json_file:

        # Открываем JSON файл для чтения
        # 'with' -  закрытие файла даже при ошибках
        # 'encoding=utf-8' - правильное чтение русских символов

        try:
            data_json = json.load(
                json_file
            )  # Пытаемся прочитать и преобразовать JSON в Python объект
        except json.JSONDecodeError:
            raise ValueError("Пустой JSON или неподдерживаемая структура")

    if not data_json or not isinstance(
        data_json, list
    ):  # Проверка что данные не пустые и являются списком
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
        writer.writeheader()  # Записываем заголовок таблицыу, использует fieldnames
        writer.writerows(data_json)
        # Записываем все данные из JSON в CSV
        # writerows() принимает список словарей и записывает каждый как строку CSV


from pathlib import Path
import json
import csv
import sys


def csv_to_json(
    csv_path: str | Path, json_path: str | Path, encoding: str = "utf-8"
) -> None:

    csv_path = Path(csv_path)  # Преобразуем входной путь CSV в объект Path
    if not csv_path.exists():  # Проверяем существование CSV файла по указанному пути
        raise FileNotFoundError("Файл не найден")

    with csv_path.open("r", encoding="utf-8") as csv_file:
        # Открываем CSV файл для чтения
        # 'with' -  закрытие файла даже при ошибках
        # 'encoding=utf-8' - правильное чтение русских символов

        read_csv = csv.DictReader(csv_file)
        # Создаем объект для чтения CSV файла, автоматически используя первую строку как заголовки
        # Преобразует каждую последующую строку в словарь с ключами (заголовков)

        if not read_csv.fieldnames:
            raise ValueError("CSV-файл не содержит заголовков или пуст")
        data_csv = (
            []
        )  # Создаем пустой список для хранения всех строк данных из CSV файла
        for row in read_csv:
            data_csv.append(
                row
            )  # Добавляем каждую строку, которая становится словарем в список
    if not data_csv:  # Проверка на существование хотя бы одной строки данных в CSV
        raise ValueError("CSV-файл пуст")

    json_path = Path(json_path)  # Преобразуем выходной путь JSON в объект Path
    with json_path.open("w", encoding="utf-8") as json_file:
        json.dump(data_csv, json_file, ensure_ascii=False, indent=2)
        # Записываем данные из списка в JSON файл
        # Преобразуем Python объекты в JSON формат и записываем в файл
        # indent=2 - добавляет отступы для читаемого форматирования


json_to_csv("data/samples/people.json", "data/out/people_from_json.csv")
csv_to_json("data/samples/people.csv", "data/out/people_from_csv.json")
