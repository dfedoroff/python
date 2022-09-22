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

def encode_rle(lst):
    str_code = ''
    prev_char = ''
    count = 1
    for char in lst:
        if char != prev_char:
            if prev_char:
                str_code += str(count) + prev_char
            count = 1
            prev_char = char
        else:
            count += 1
    return str_code

def decode_rle(lst:str):
    count = ''
    str_decode = ''
    for char in lst:
        if char.isdigit():
            count += char
        else:
            str_decode += char * int(count)
            count = ''
    return str_decode