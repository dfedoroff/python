# Погружение в Python, Часть 1. Файлы и файловая система, Семинар 7, hw7-1
#
# -----------------
# Задача 1:
# Напишите функцию группового переименования файлов. Она должна:
# a. принимать параметр желаемое конечное имя файлов. При переименовании в
#    конце имени добавляется порядковый номер.
# b. принимать параметр количество цифр в порядковом номере.
# c. принимать параметр расширение исходного файла. Переименование должно
#    работать только для этих файлов внутри каталога.
# d. принимать параметр расширение конечного файла.
# e. принимать диапазон сохраняемого оригинального имени. Например для
#    диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла.
#    К ним прибавляется желаемое конечное имя, если оно передано.
#    Далее счётчик файлов и расширение.

import os


def filter_files(directory, source_ext):
    all_files = os.listdir(directory)
    target_files = [f for f in all_files if f.endswith(source_ext)]
    untouched_files = [f for f in all_files if not f.endswith(source_ext)]
    return target_files, untouched_files


def construct_new_filename(name_part, desired_name, count, digits_num, destination_ext):
    return f"{name_part}{desired_name}{str(count).zfill(digits_num)}{destination_ext}"
