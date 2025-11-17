import argparse
import sys
from pathlib import Path
from src.lib.text import tokenize, count_freq, top_n


def main():
    parser = argparse.ArgumentParser(
        description="CLI-утилиты"
    )  # Создаем главный парсер аргументов
    subparsers = parser.add_subparsers(
        dest="command"
    )  # Создаем контейнер для подкоманд (cat и stats)

    cat_parser = subparsers.add_parser(
        "cat", help="Вывести содержимое файла"
    )  # Создаем парсер для команды
    cat_parser.add_argument(
        "--input", required=True, help="Путь к входному файлу"
    )  # Добавляем обязательный аргумент
    cat_parser.add_argument(
        "--number", action="store_true", help="Нумеровать строки"
    )  # Добавляем опциональный флаг -n для нумерации строк

    stats_parser = subparsers.add_parser("stats", help="Частоты слов в тексте")
    stats_parser.add_argument("--input", required=True, help="Путь к текстовому файлу")
    stats_parser.add_argument(
        "--top", type=int, default=5, help="Количество наиболее частых слов"
    )
    if len(sys.argv) == 1:  # Проверка: на наличие аргументов при вводе
        parser.error("Необходимо указать команду")

    args = (
        parser.parse_args()
    )  # Парсим аргументы командной строки, переданные при запуске программы
    filepath = Path(args.input)  # Преобразуем строку пути в объект Path

    if not filepath.exists():
        raise FileNotFoundError("Файл не найден")
    if args.command == "cat":
        with filepath.open("r", encoding="utf-8") as f:
            line_number = 1  # Счетчик строк
            for line in f:  # Читаем файл построчно
                line = line.rstrip("\n")  # удаляем символ перевода строки
                if args.number:  # Если нумерация введена, выводим строку с ее номером
                    print(f"{line_number}: {line}")
                    line_number += 1
                else:
                    print(line)
    elif args.command == "stats":
        with filepath.open("r", encoding="utf-8") as file:
            text_lines = file.readlines()
        full_text = "".join(text_lines)
        tokens = tokenize(text=full_text)
        freq = count_freq(tokens=tokens)
        top = top_n(freq=freq, n=args.top)
        for word, count in top:
            print(f"{word} - {count}")


if (
    __name__ == "__main__"
):  # Точка входа в программу - код выполнится только при прямом запуске файла
    main()
