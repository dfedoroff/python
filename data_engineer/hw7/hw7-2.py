# Погружение в Python, Часть 1. Файлы и файловая система, Семинар 7, hw7-2
#
# -----------------
# Задача 2:
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет
# для работы с файлами.

import random


_MIN_VALUE, _MAX_VALUE = -1000, 1000
_DELIMITER = "|"
_VOWELS, _CONSONANTS = "AEIOUY", "BCDFGHJKLMNPQRSTVWXYZ"
_MIN_LEN, _MAX_LEN = 4, 7


def fill_file_with_numbers(filename, lines_count):
    with open(filename, "a", encoding="utf-8") as file:
        for _ in range(lines_count):
            ints = random.randint(_MIN_VALUE, _MAX_VALUE)
            floats = random.uniform(_MIN_VALUE, _MAX_VALUE)
            file.write(f"{ints}{_DELIMITER}{floats}\n")


def generate_name():
    length = random.randint(_MIN_LEN, _MAX_LEN)
    name = "".join(random.choice(_VOWELS if i % 3 == 0 else _CONSONANTS) for i in range(length))
    return name.capitalize()


def fill_file_with_names(filename, names_count):
    with open(filename, "w", encoding="utf-8") as file:
        names = [generate_name() for _ in range(names_count)]
        file.write("\n".join(names))
