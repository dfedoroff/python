# Данные, функции и модули в Python, Семинар 3, hw3-2
#
# -----------------
# Задача 2:
# Напишите программу, которая найдёт произведение пар чисел
# списка.Парой считаем первый и последний элемент, второй и
# предпоследний и т.д
#
# Пример:
# [2, 3, 4, 5, 6] -> [12, 15, 16];
# [2, 3, 5, 6] -> [12, 15]

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