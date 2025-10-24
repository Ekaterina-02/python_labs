### B номер 
import sys
from lib.text import normalize, tokenize, count_freq, top_n

def text_statistics():
    text_vvod=sys.stdin  # получаем объект для чтения ввода с клавиатуры
    text=text_vvod.read()  # читаем весь текст, который ввели до нажатия Ctrl+D
    if text=='':
        print('нет введенного текста')
        return
    normalize_text=normalize(text)
    tokenize_text=tokenize(normalize_text)
    count_freq_text=count_freq(tokenize_text)
    top_n_text=top_n(count_freq_text,5)
    print(f'Всего слов: {len(tokenize_text)}')
    print(f'Уникальных слов: {len(set(tokenize_text))}')
    print("Топ-5:")  # заголовок для списка самых частых слов
    for word, count in top_n_text:
        print(f"{word}:{count}")
if __name__ == "__main__":  # проверяем, запущен ли файл как основная программа
    text_statistics()
