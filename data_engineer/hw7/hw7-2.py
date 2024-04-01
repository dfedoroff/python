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
