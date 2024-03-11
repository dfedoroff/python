# Погружение в Python, Часть 1. Основы Python, Семинар 1, hw1-2
#
# -----------------
# Задача 2:
# Напишите код, который запрашивает число и сообщает является ли
# оно простым или составным. Используйте правило для проверки:
# "Число является простым, если делится нацело только на единицу
# и на себя". Сделайте ограничение на ввод отрицательных чисел и
# чисел больше 100 000.

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def get_number_input():
    while True:
        try:
            number = int(input("Введите число от 0 до 100000: "))
            if 0 <= number <= 100000:
                return number
            else:
                print("Число должно быть в диапазоне от 0 до 100000.")
        except ValueError:
            print("Пожалуйста, введите корректное целое число.")


def main():
    number = get_number_input()
    if number in (0, 1):
        result = f"Число {number} - ни простое, ни составное."
    elif is_prime(number):
        result = f"Число {number} - простое."
    else:
        result = f"Число {number} - составное."
    print(result)


if __name__ == "__main__":
    main()
