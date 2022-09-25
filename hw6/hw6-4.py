# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip,
# enumerate, list comprehension. Продолжение, Семинар 6, hw6-4
#
# -----------------
# Задача 4:
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random

def find_polynomial(k):
    result = "".join([str(random.randint(0, 100)) + "X^" + str(i) + "+" for i in range(k, 0, -1)])
    return result

k = int(input('Введите натуральную степень k = '))
print(find_polynomial(k)[:-1])
