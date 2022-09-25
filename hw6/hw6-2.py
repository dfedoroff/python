# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip,
# enumerate, list comprehension. Продолжение, Семинар 6, hw6-2
#
# -----------------
# Задача 2:
# Задайте последовательность чисел. Напишите программу,
# которая выведет список неповторяющихся элементов
# исходной последовательности.
#
# Пример:
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]

def find_duplicates(lst):
    result = list(filter(lambda i: lst.count(i) == 1, lst))
    return result

lst = [1, 1, 2, 3, 4, 5, 5]
print(f'Оригинальный список: {lst}')
print(f'Неповторяющиеся элементы: {find_duplicates(lst)}')
