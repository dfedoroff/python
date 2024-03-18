# Погружение в Python, Часть 1. Коллекции, Семинар 3, hw3-3
#
# -----------------
# Задача 3:
# Создайте словарь со списком вещей для похода в качестве ключа
# и их массой в качестве значения. Определите какие вещи влезут
# в рюкзак передав его максимальную грузоподъёмность.
# Достаточно вернуть один допустимый вариант.
# *Верните все возможные варианты комплектации рюкзака.

import random


def generate_items():
    return {
        "tent": 50,
        "food": 20,
        "water": 30,
        "clothes": 10,
        "flashlight": 5,
        "map": 2,
        "knife": 3
    }


def find_packing_combinations(items, max_load):
    selected_items = []
    current_weight = 0
    items_list = list(items.items())
    random.shuffle(items_list)  # Для обеспечения разнообразия результатов
    for item, weight in items_list:
        if current_weight + weight <= max_load:
            selected_items.append((item, weight))
            current_weight += weight
    return selected_items, current_weight
