import argparse
from src.lab05.json_csv import json_to_csv, csv_to_json
from src.lab05.csv_xlsx import csv_to_xlsx


def main():
    parser = argparse.ArgumentParser(
        description="CLI-утилиты"
    )  # Создаем главный парсер аргументов
    subparsers = parser.add_subparsers(
        dest="command"
    )  # Создаем контейнер для подкоманд, выбранная команда сохраненится в args.command

    json2csv_parser = subparsers.add_parser(
        "json2csv", help="Конвертировать JSON в CSV"
    )  # Создаем парсер для команды
    json2csv_parser.add_argument(
        "--input", required=True, help="Путь к JSON-файлу"
    )  # Добавляем обязательный аргумент --input
    json2csv_parser.add_argument(
        "--output", required=True, help="Путь для CSV-файла"
    )  # Добавляем обязательный аргумент --output

    csv2json_parser = subparsers.add_parser(
        "csv2json", help="Конвертировать CSV в JSON"
    )
    csv2json_parser.add_argument("--input", required=True, help="Путь к CSV-файлу")
    csv2json_parser.add_argument("--output", required=True, help="Путь для JSON-файла")

    csv2xlsx_parser = subparsers.add_parser(
        "csv2xlsx", help="Конвертировать CSV в XLSX"
    )
    csv2xlsx_parser.add_argument("--input", required=True, help="Путь к CSV-файлу")
    csv2xlsx_parser.add_argument("--output", required=True, help="Путь для XLSX-файла")

    args = (
        parser.parse_args()
    )  # Парсим аргументы командной строки, переданные при запуске программы
    if args.command == "json2csv":  # Проверяем, какую команду выбрали
        json_to_csv(json_path=args.input, csv_path=args.output)
        # передаем входной файл из аргумента --input, выходной файл из аргумента --output

    elif args.command == "csv2json":
        csv_to_json(csv_path=args.input, json_path=args.output)

    elif args.command == "csv2xlsx":
        csv_to_xlsx(csv_path=args.input, xlsx_path=args.output)


if (
    __name__ == "__main__"
):  # Точка входа в программу - код выполнится только при прямом запуске файла
    main()
