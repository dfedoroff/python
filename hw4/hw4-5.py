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

def write_file(name, poly):
    with open(name, 'w') as data:
        data.write(poly)

def read_poly(file):
    with open(str(file), 'r') as data:
        poly = data.readlines()
    return poly

def find_sqrt_poly(k):
    if 'x^' in k:
        i = k.find('^')
        result = int(k[i + 1:])
    elif ('x' in k) and ('^' not in k):
        result = 1
    else:
        result = -1
    return result

def find_coef_poly(k):
    if 'x' in k:
        i = k.find('x')
        result = int(k[:i])
    return result

def calc_poly(poly):
    poly = poly[0].replace(' ', '').split('=')
    poly = poly[0].split('+')
    lst = []
    l = len(poly)
    k = 0
    if find_sqrt_poly(poly[-1]) == -1:
        lst.append(int(poly[-1]))
        l -= 1
        k = 1
    sqrt = 1
    i = l - 1
    while i >= 0:
        if (find_sqrt_poly(poly[i]) != -1) and (find_sqrt_poly(poly[i]) == sqrt):
            lst.append(find_coef_poly(poly[i]))
            i -= 1
            sqrt += 1
        else:
            lst.append(0)
            sqrt += 1
    return lst

def sum_poly(poly1, poly2):
    lst1 = calc_poly(poly1)
    lst2 = calc_poly(poly2)
    l = len(lst1)
    if len(lst1) > len(lst2):
        l = len(lst2)
    lst_new = [lst1[i] + lst2[i] for i in range(l)]
    if len(lst1) > len(lst2):
        m = len(lst1)
        for i in range(l, m):
            lst_new.append(lst1[i])
    else:
        m = len(lst2)
        for i in range(l, m):
            lst_new.append(lst2[i])
    return lst_new

def create_poly(sum_p):
    lst = sum_p[::-1]
    result = ''
    if len(lst) < 1:
        result = 'x = 0'
    else:
        for i in range(len(lst)):
            if (i != len(lst) - 1) and (lst[i] != 0) and (i != len(lst) - 2):
                result += f'{lst[i]}x^{len(lst) - i - 1}'
                if (lst[i + 1] != 0) or (lst[i + 2] != 0):
                    result += ' + '
            elif (i == len(lst) - 2) and (lst[i] != 0):
                result += f'{lst[i]}x'
                if (lst[i + 1] != 0) or (lst[i + 2] != 0):
                    result += ' + '
            elif (i == len(lst) - 1) and (lst[i] != 0):
                result += f'{lst[i]} = 0'
            elif (i == len(lst) - 1) and (lst[i] == 0):
                result += ' = 0'
    return result

k1 = int(input('Введите натуральную степень 1-го многочлена = '))
k2 = int(input('Введите натуральную степень 2-го многочлена = '))
polynomial1 = find_polynomial(k1)
print(f'1-й многочлен: {polynomial1}')
polynomial2 = find_polynomial(k2)
print(f'2-й многочлен: {polynomial2}')
write_file('polynominal_1.txt', polynomial1)
write_file('polynominal_2.txt', polynomial2)
polynomial1 = read_poly('polynominal_1.txt')
polynomial2 = read_poly('polynominal_2.txt')
sum_polynominals = sum_poly(polynomial1, polynomial2)
print(f'Сумма многочленов: {create_poly(sum_polynominals)}')