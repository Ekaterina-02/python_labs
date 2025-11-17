import csv
import json
from pathlib import Path
import pytest
from src.lab05.json_csv import csv_to_json, json_to_csv


def write_json(path: Path, obj):  # Функция для записи JSON файла
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2), encoding="utf-8")


def read_csv_rows(path: Path):  # Функция для чтения CSV файла
    with path.open(encoding="utf-8") as f:
        return list(
            csv.DictReader(f)
        )  # читает CSV и преобразует каждую строку в список словарей


def test_json_to_csv_roundtrip(tmp_path: Path):
    src = tmp_path / "people.json"  # Создаем путь к исходному файлу во временной папке
    dst = tmp_path / "people.csv"  # Создаем путь к целевому файлу во временной папке
    data = [
        {"name": "Alice", "age": 22},
        {"name": "Bob", "age": 25},
    ]  # Вводим тестовые данные
    write_json(src, data)  # Записываем тестовые данные в JSON файл

    json_to_csv(str(src), str(dst))
    rows = read_csv_rows(dst)  # Читаем результат CSV файла
    assert len(rows) == 2
    assert set(rows[0]) >= {
        "name",
        "age",
    }  # В первой строке должны быть хотя бы колонки "name" и "age" (может быть больше)


def test_csv_to_json_roundtrip(tmp_path: Path):
    src = tmp_path / "people.csv"
    dst = tmp_path / "people.json"
    src.write_text(
        "name,age\nAlice,22\nBob,25\n", encoding="utf-8"
    )  # Создаем CSV файл с заголовком и двумя строками

    csv_to_json(str(src), str(dst))
    obj = json.loads(dst.read_text(encoding="utf-8"))
    assert (
        isinstance(obj, list) and len(obj) == 2
    )  # должен быть списком и содержать 2 элемента
    assert set(obj[0]) == {
        "name",
        "age",
    }  # В первом элементе должны быть олько ключи "name" и "age"(не должно быть лишних)


def test_json_to_csv_empty_raises(
    tmp_path: Path,
):  # Проверка обработки пустого JSON файла
    src = tmp_path / "empty.json"
    src.write_text("[]", encoding="utf-8")
    with pytest.raises(ValueError):
        json_to_csv(str(src), str(tmp_path / "out.csv"))


def test_csv_to_json_no_header_raises(
    tmp_path: Path,
):  # Проверка обработки CSV файла без заголовка
    src = tmp_path / "bad.csv"
    src.write_text("", encoding="utf-8")
    with pytest.raises(ValueError):
        csv_to_json(str(src), str(tmp_path / "out.json"))


def test_missing_file_raises():  # Тест 5: Проверка обработки несуществующего файла
    with pytest.raises(FileNotFoundError):
        csv_to_json("nope.csv", "out.json")
