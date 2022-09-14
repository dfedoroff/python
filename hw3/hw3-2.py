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

def mult_pairs(lst_num):
    lst_pairs = []
    for i in range((len(lst_num) + 1) // 2):
        lst_pairs.append(lst_num[i] * lst_num[len(lst_num) - 1 - i])
    return lst_pairs

num = int(input('Введите количество элементов списка: '))
start = int(input('Введите начало диапазона: '))
end = int(input('Введите конец диапазона: '))
rand_list = rand(num, start, end)
print(f'Cписок случайных чисел: {rand_list}')