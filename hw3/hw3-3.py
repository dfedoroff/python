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

num = int(input('Введите количество элементов списка: '))
start = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))
rand_list = rand(num, start, end)