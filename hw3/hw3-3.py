# Данные, функции и модули в Python, Семинар 3, hw3-3
#
# -----------------
# Задача 3:
# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным
# значением дробной части элементов.
#
# Пример:
# [1.1, 1.2, 3.1, 10.01] -> 0.19

import random

def rand(num, start, end):
    lst = []
    for i in range(num):
        n = round(random.uniform(start, end), 2)
        lst.append(n)
    return lst

def find_diff(lst_num):
    max_num = lst_num[0]%1
    min_num = lst_num[0]%1
    for i in range(1, len(lst_num)):
        if lst_num[i]%1 > max_num:
            max_num = lst_num[i]%1
        elif lst_num[i]%1 < min_num:
            min_num = lst_num[i]%1
    diff = max_num - min_num
    return diff, max_num, min_num

num = int(input('Введите количество элементов списка: '))
start = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))
rand_list = rand(num, start, end)
print(f'Cписок случайных чисел: {rand_list}')