# Погружение в Python, Часть 1. Коллекции, Семинар 3, hw3-2
#
# -----------------
# Задача 2:
# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.

import re
from collections import Counter


def read_and_clean_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().lower()
    cleaned_text = re.sub(r"[\W_]+", " ", text)
    return cleaned_text


def get_top_10_words(text):
    words = text.split()
    word_counts = Counter(words)
    top_10_words = word_counts.most_common(10)
    return top_10_words


def write_top_10_to_file(top_10_words, output_file_path):
    with open(output_file_path, "w", encoding="utf-8") as output_file:
        for word, count in top_10_words:
            output_file.write(f"{word} - {count}\n")


def process_file(input_file_path, output_file_path):
    text = read_and_clean_text(input_file_path)
    top_10_words = get_top_10_words(text)
    write_top_10_to_file(top_10_words, output_file_path)


def main():
    input_file_path = "text.txt"
    output_file_path = "top_10_words.txt"
    process_file(input_file_path, output_file_path)


if __name__ == "__main__":
    main()
