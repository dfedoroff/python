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

from random import randint, choice

rules = ('Привет! Это игра "Забери все конфеты!" Ее основные правила: '
            'Участникам дана 2021 конфета, но за один ход можно взять не более 28.')

messages = ['Ваша очередь брать конфеты ', 'возьмите конфеты ',
            'сколько конфет возьмёте? ', 'берите, не стесняйтесь ', 'Ваш ход ']

def introduce_players():
    player1 = input('Представьтесь, пожалуйста: ')
    player2 = 'ИИ'
    print(f'Очень приятно, меня зовут {player2}')
    return [player1, player2]

def get_rules(players):
    n = 2021
    m = 28
    first = int(input(f'{players[0]}, если хотите ходить первым, нажмите 1, если нет, любую другую клавишу. '))
    if first != 1:
        first = 0
    return [n, m, int(first)]

def play_game(rules, players, messages):
    count = rules[2]
    if (rules[0] % 10 == 1) and (9 > rules[0] > 10):
        letter = 'а'
    elif (1 < rules[0] % 10 < 5) and (9 > rules[0] > 10):
        letter = 'ы'
    else:
        letter = ''
    while rules[0] > 0:
        if not count % 2:
            move = randint(1, rules[1])
            print(f'Я забираю {move}')
        else:
            print(f'{players[0]}, {choice(messages)}')
            move = int(input())
            if (move > rules[0]) or (move > rules[1]):
                print(f'Это слишком много, можно взять не более {rules[1]} конфет{letter}, у нас всего {rules[0]} конфет{letter}')
                attempt = 3
                while attempt > 0:
                    if rules[0] >= move <= rules[1]:
                        break
                    print(f'Попробуйте ещё раз, у Вас {attempt} попытки')
                    move = int(input())
                    attempt -= 1
                else:
                    return print(f'Очень жаль, у Вас не осталось попыток. Game over!')
        rules[0] = rules[0] - move
        if rules[0] > 0:
            print(f'Осталось {rules[0]} конфет{letter}')
        else:
            print('Все конфеты разобраны.')
        count += 1
    return players[count % 2]

def find_winner (rules, players, messages):
    winner = play_game(rules, players, messages)
    if not winner:
        print('Победителя нет.')
    else:
        print(f'В этот раз победил {winner}! Ему достаются все конфеты!')

print(rules)
players = introduce_players()
rules = get_rules(players)