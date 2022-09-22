# Ускоренная обработка данных: lambda, filter, map, zip, enumerate,
# list comprehension. Семинар 5, hw5-3
#
# -----------------
# Задача 3:
# Создайте программу для игры в "Крестики-нолики".

board = list(range(1, 10))

def print_board(table):
    for i in range(3):
        print(table[0 + i * 3], table[1 + i * 3], table[2 + i * 3])