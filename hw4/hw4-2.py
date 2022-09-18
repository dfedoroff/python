# Данные, функции и модули в Python. Семинар 4, hw4-2
#
# -----------------
# Задача 2:
# Задайте натуральное число N. Напишите программу,
# которая составит список простых множителей числа N.
#
# Пример:
# 20 -> [2, 2, 5]

def find_simple_multipliers(n):
    simple_mult = 2
    lst = []
    while simple_mult <= n:
        if n % simple_mult == 0:
            lst.append(simple_mult)
            n //= simple_mult
        else:
            simple_mult += 1
    return lst

n = int(input('Введите число: '))
print(f'Простые множители числа {n}: {find_simple_multipliers(n)}')