# Данные, функции и модули в Python. Семинар 4, hw4-4
#
# -----------------
# Задача 4:
# Задана натуральная степень k. Сформировать случайным
# образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
#
# Пример:
# k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

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

def write_file(output):
    with open('polynominal.txt', 'w+') as data:
        data.write(output)
    print(f'Файл с многочленом записан.')

k = int(input('Введите натуральную степень k = '))
polynomial = find_polynomial(k)
print(f'Многочлен в степени {k}: {polynomial}')
write_file(polynomial)