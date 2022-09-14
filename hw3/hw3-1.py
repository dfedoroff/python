# Данные, функции и модули в Python, Семинар 3, hw3-1
#
# -----------------
# Задача 1:
# Задайте список из нескольких чисел. Напишите программу,
# которая найдёт сумму элементов списка, стоящих на
# нечётной позиции.
#
# Пример:
# [2, 3, 5, 9, 3] -> 12

import random

def rand(num, start, end):
    lst = []
    for i in range(num):
        n = random.randint(start, end)
        lst.append(n)
    return lst

num = int(input('Введите количество элементов списка: '))
start = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))
rand_list = rand(num, start, end)