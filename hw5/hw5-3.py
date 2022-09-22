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

def make_move(move, symbol):
    i = board.index(move)
    board[i] = symbol

def find_winner():
    win_coord = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    win = ''
    for i in win_coord:
        if (board[i[0]] == '\u001B[34mX\u001b[0m' and board[i[1]]) == ('\u001B[34mX\u001b[0m' and board[i[2]]) == ('\u001B[34mX\u001b[0m'):
            win = '\u001B[34mигрок 1\u001b[0m'
        if (board[i[0]] == '\u001B[31mO\u001b[0m' and board[i[1]]) == ('\u001B[31mO\u001b[0m' and board[i[2]]) == ('\u001B[31mO\u001b[0m'):
            win = '\u001B[31mигрок 2\u001b[0m'
    return win
