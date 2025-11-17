import sys

# Получаем список всех путей
sys.path.append("C:/Users/HP/Desktop/python_labs/src")
from lib.text import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv

# read_text - функция для чтения текстовых файлов
# write_csv - функция для записи данных в CSV файлы

try:
    raw_text = read_text(
        "data/lab04/neinput.txt"
    )  # Пытаемся прочитать файл 'data/lab04/input.txt'
except FileNotFoundError as e:  # Если файл не найден, то инфа об ошибке пишется в e
    print(f"Ошибка: {e}")  # в f-строке - детали ошибки из переменной 'e'
    sys.exit(1)  # Завершаем программу с кодом ошибки 1

raw_text = tokenize(normalize(raw_text))
word = count_freq(raw_text)
text_counts = top_n(word)
print("Всего слов:", len(raw_text))
print("Уникальных слов:", len(set(raw_text)))
print("Топ-5:")
for i in text_counts:
    print(f"{i[0]}:{i[1]}")
write_csv(text_counts, "data/lab04/report.csv", ("word", "count"))

# Записываем результаты анализа в CSV файл
# text_counts - список кортежей для записи
# 'data/lab04/report.csv' - путь к файлу
# ("word","count") - заголовок таблицы
