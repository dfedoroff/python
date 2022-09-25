# Урок 6. Ускоренная обработка данных: lambda, filter, map, zip,
# enumerate, list comprehension. Продолжение, Семинар 6, hw6-1
#
# -----------------
# Задача 1:
# Задайте список из N элементов, заполненных числами из
# промежутка [-N, N].

def fill_lst(n):
    lst = [i for i in range(-n, n + 1)]
    return lst

n = int(input('Введите число: '))
print(f'Числа из промежутка [{-n}, {n}]: {fill_lst(n)}')
