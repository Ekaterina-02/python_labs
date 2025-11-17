from pathlib import (
    Path,
)  # Импортируем класс Path из модуля pathlib для работы с путями файлов


def read_text(path: str | Path, encoding: str = "utf-8") -> str:

    # path - строка или объект Path (путь к файлу)
    # encoding - кодировка файла, по умолчанию utf-8
    # -> str - функция возвращает строку (содержимое файла)

    p = Path(path)  # Преобразуем переданный путь в объект Path для удобной работы
    if not p.exists():  # Проверка существования файла по указанному пути
        raise FileNotFoundError("Файл не найден")

        """
        Выбор другой кодировки:
        в кодировке по умолчанию (UTF-8):
        read_text("file.txt")
        в кодировке Windows-1251:
        read_text("file.txt", encoding="cp1251")
        в кодировке KOI8-R:
        read_text("file.txt", encoding="koi8-r")
        """

    return p.read_text(
        encoding=encoding
    )  # Читаем и возвращаем файл в указанной кодировке


import csv
from pathlib import Path  # Импортируем класс Path для работы с путями файлов
from typing import Iterable, Sequence  # Импортируем типы данных

# Iterable - означает "что-то, по чему можно пройтись циклом for"
# Sequence - означает "что-то упорядоченное, к элементам можно обращаться по индексу"


def write_csv(
    rows: Iterable[Sequence], path: str | Path, header: tuple[str, ...] | None = None
) -> None:
    """
    rows - данные для записи
    path - путь к файлу (может быть строкой или объектом Path)
    header - заголовок таблицы (кортеж строк или None, если заголовка нет)
    -> None -не возвращает никакого значения
    """
    p = Path(path)
    rows = list(rows)  # Содаем список для многоразового обращения к данным
    with p.open("w", newline="", encoding="utf-8") as f:
        # 'w' - режим записи
        # newline='' - отключаем автоматическую обработку переносов строк
        # encoding='utf-8' - устанавливаем кодировку UTF-8
        # as f - создаем переменную f для работы с файлом
        w = csv.writer(f)  # Создаем объект writer для записи данных
        if header is not None:
            w.writerow(header)  # Записываем заголовок как первую строку в CSV файл
        if rows:
            for row in rows:
                if len(row) != len(rows[0]):
                    raise ValueError("Строки имеют разную длину!")
        for row in rows:
            w.writerow(row)  # Записываем текущую строку в CSV файл ничего не возвращая
