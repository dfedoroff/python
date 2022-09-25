# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip,
# enumerate, list comprehension. Продолжение, Семинар 6, hw6-3
#
# -----------------
# Задача 3:
# Напишите программу, которая найдёт произведение пар чисел
# списка. Парой считаем первый и последний элемент, второй и
# предпоследний и т.д
#
# Пример:
# [2, 3, 4, 5, 6] -> [12, 15, 16];
# [2, 3, 5, 6] -> [12, 15]

def mult_pairs(lst):
    result = [lst[i] * lst[len(lst) - 1 - i] for i in range((len(lst) // 2) + 1)]
    return result

lst = [2, 3, 4, 5, 6]
print(f'Оригинальный список: {lst}')
print(f'Произведение пар чисел списка: {mult_pairs(lst)}')
