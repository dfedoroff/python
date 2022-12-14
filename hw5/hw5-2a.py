# Ускоренная обработка данных: lambda, filter, map, zip, enumerate,
# list comprehension. Семинар 5, hw5-2
#
# -----------------
# Задача 2:
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход
# друг после друга. Первый ход определяется жеребьёвкой. За один ход можно
# забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему
# последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все
# конфеты у своего конкурента?
# a) Добавьте игру против бота.
# b) Подумайте как наделить бота "интеллектом".

import random

rules = ('Привет! Это игра "Забери все конфеты!" Ее основные правила: '
            'Участникам дана 2021 конфета, но за один ход можно взять не более 28.')

messages = ['Ваша очередь брать конфеты', 'возьмите конфеты',
            'сколько конфет возьмёте?', 'берите, не стесняйтесь', 'Ваш ход']

def play_game(n, m, players, messages):
    count = 0
    if n % 10 == 1 and 9 > n > 10:
        letter = 'а'
    elif 1 < n % 10 < 5 and 9 > n > 10:
        letter = 'ы'
    else:
        letter = ''
    while n > 0:
        print(f'{players[count % 2]}, {random.choice(messages)}')
        move = int(input())
        if move > n or move > m:
            print(f'Слишком много! Можно взять не более {m} конфет{letter}, у нас всего {n} конфет{letter}')
            attempt = 3
            while attempt > 0:
                if n >= move <= m:
                    break
                print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                move = int(input())
                attempt -= 1
            else:
                return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        n = n - move
        if n > 0:
            print(f'Осталось {n} конфет{letter}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[not count % 2]

def find_winner (n, m, players, messages):
    winner = play_game(n, m, players, messages)
    if not winner:
        print('Победителя нет.')
    else:
        print(f'В этот раз победил {winner}! Ему достаются все конфеты!')

print(rules)
player1 = input('Представьтесь, пожалуйста: ')
player2 = input('Представьтесь, пожалуйста: ')
players = [player1, player2]
n = 2021
m = 28
find_winner(n, m, players, messages)