# Погружение в Python, Часть 1. Функции, Семинар 4, hw4-1
#
# -----------------
# Задача 1:
# Напишите функцию для транспонирования матрицы.

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]

