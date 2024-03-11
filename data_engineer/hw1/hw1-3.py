# Погружение в Python, Часть 1. Основы Python, Семинар 1, hw1-3
#
# -----------------
# Задача 3:
# Программа загадывает число от 0 до 1000. Необходимо угадать
# число за 10 попыток. Программа должна подсказывать "больше" или
# "меньше" после каждой попытки. Для генерации случайного числа
# используйте код:
# from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)

from random import randint


def guess_the_number(lower_limit=0, upper_limit=1000, attempts=10):
    secret_number = randint(lower_limit, upper_limit)
    for attempt in range(1, attempts + 1):
        try:
            user_guess = int(input(f"Попытка {attempt}. Введите целое число: "))
        except ValueError:
            print("Пожалуйста, введите корректное целое число.")
            continue
        if user_guess == secret_number:
            print(f"Вы угадали число {secret_number}!")
            return
        elif secret_number < user_guess:
            print(f"Загаданное число меньше {user_guess}.")
        else:
            print(f"Загаданное число больше {user_guess}.")
    print("Попытки закончились, число НЕ угадано.")


guess_the_number()
