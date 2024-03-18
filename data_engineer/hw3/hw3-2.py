# Погружение в Python, Часть 1. Коллекции, Семинар 3, hw3-2
#
# -----------------
# Задача 2:
# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью из википедии
# или из документации к языку.

import re


def read_and_clean_text(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        text = file.read().lower()
    cleaned_text = re.sub(r"[\W_]+", " ", text)
    return cleaned_text