# Данные, функции и модули в Python. Семинар 4, hw4-1
#
# -----------------
# Задача 1:
# Вычислить число c заданной точностью d.
#
# Пример:
# при d = 0.001, π = 3.141

def round_with_precision(d):
    prec = len(d) - 2
    result = 0
    k = 1
    for i in range(1000000):
        if i % 2 == 0:
            result += 4 / k
        else:
            result -= 4 / k
        k += 2
    return result, prec

d = input('Задайте точность числа Пи от 0.1: ')