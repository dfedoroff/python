# Погружение в Python, Часть 1. Коллекции, Семинар 3, hw3-1
#
# -----------------
# Задача 1:
# Дан список повторяющихся элементов. Вернуть список с
# дублирующимися элементами. В результирующем списке не должно
# быть дубликатов.

import random


def generate_random_list(size, min_value, max_value):
    return [random.randint(min_value, max_value) for _ in range(size)]


def find_duplicates(input_list):
    return list({element for element in input_list if input_list.count(element) > 1})
