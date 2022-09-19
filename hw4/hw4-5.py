# Данные, функции и модули в Python. Семинар 4, hw4-5
#
# -----------------
# Задача 5:
# Даны два файла, в каждом из которых находится запись
# многочлена. Задача - сформировать файл, содержащий
# сумму многочленов.

from random import randint

def find_polynomial(k):
    ratios = [str(randint(0, 100)) for i in range(k + 1)]
    result = ''
    for i in range(0, k + 1):
        if i == k:
            result += ratios[i] + ' = 0'
        elif i == k - 1:
            result += ratios[i] + 'x + '
        elif i < k - 1:
            result += ratios[i] + 'x^' + str(k - i) + ' + '
    return result

k1 = int(input('Введите натуральную степень 1-го многочлена = '))
k2 = int(input('Введите натуральную степень 2-го многочлена = '))
polynomial1 = find_polynomial(k1)
print(f'1-й многочлен: {polynomial1}')
polynomial2 = find_polynomial(k2)
print(f'2-й многочлен: {polynomial2}')