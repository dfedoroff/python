# Ускоренная обработка данных: lambda, filter, map, zip, enumerate,
# list comprehension. Семинар 5, hw5-4
#
# -----------------
# Задача 4:
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

def read_file(file):
    with open(file, 'r') as data:
        text = data.read()
    return text
