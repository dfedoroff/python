# Погружение в Python, Часть 1. Итераторы и генераторы, Семинар 5, hw5-1
#
# -----------------
# Задача 1:
# Напишите функцию, которая принимает на вход строку - абсолютный путь до
# файла. Функция возвращает кортеж из трёх элементов: путь, имя файла,
# расширение файла.

import os


def extract_file_info(absolute_path):
    path, full_filename = os.path.split(absolute_path)
    filename, extension = os.path.splitext(full_filename)
    return (path, filename, extension)
