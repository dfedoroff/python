# Погружение в Python, Часть 1. Модули, Семинар 6, hw6-3
#
# -----------------
# Задача 3:
# Напишите функцию в шахматный модуль. Используйте генератор
# случайных чисел для случайной расстановки ферзей в задаче
# выше. Проверяйте различный случайные варианты и выведите
# 4 успешных расстановки.

import random


def is_queens_safe(queens):
    for i in range(8):
        for j in range(i + 1, 8):
            if queens[i] == queens[j] or \
               abs(queens[i][0] - queens[j][0]) == abs(queens[i][1] - queens[j][1]):
                return False
    return True


def generate_random_queens():
    positions = [(i, random.randint(1, 8)) for i in range(1, 9)]
    return positions
