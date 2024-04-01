# Погружение в Python, Часть 1. Файлы и файловая система, Семинар 7, hw7-2
#
# -----------------
# Задача 2:
# Соберите из созданных на уроке и в рамках домашнего задания функций пакет
# для работы с файлами.

import random
import itertools


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


def multiply_numbers_and_associate_with_names(numbers_file, names_file, result_file):
    with open(numbers_file, encoding="utf-8") as nums, open(names_file, encoding="utf-8") as names:
        numbers = (line.split(_DELIMITER) for line in nums)
        products = (int(n) * float(f) for n, f in numbers)
        names = names.read().splitlines()
        with open(result_file, "w", encoding="utf-8") as result:
            for name, product in zip(itertools.cycle(names), products):
                result_name = name.lower() if product < 0 else name.upper()
                product_value = abs(product) if product < 0 else round(product)
                result.write(f"{result_name} - {product_value}\n")


def create_file_with_extension(extension, min_len=6, max_len=30, min_bytes=256, max_bytes=4096, files_count=42):
    for _ in range(files_count):
        name_length = random.randint(min_len, min(max_len, 26))
        name = ''.join(random.choices("abcdefghijklmnopqrstuvwxyz", k=name_length))
        filename = f"{name}.{extension}"
        with open(filename, "wb") as file:
            file.write(random.randbytes(random.randint(min_bytes, max_bytes)))


def generate_files_with_extensions(extensions):
    for extension in extensions:
        create_file_with_extension(extension, files_count=1)
