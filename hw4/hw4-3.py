# Данные, функции и модули в Python. Семинар 4, hw4-3
#
# -----------------
# Задача 3:
# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов
# исходной последовательности.
#
# Пример:
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

import re

def find_duplicates(lst):
    input_list = list(map(int, re.split(r'[, ;]', lst))) # split string by multiple delimiters ',' ' ' ';'
    output_list = []
    for i in input_list:
        if i not in output_list:
            output_list.append(i)
    return output_list

lst = input('Введите числа: ')
print(f'Список неповторяющихся элементов: {find_duplicates(lst)}')