# Погружение в Python, Часть 1. Итераторы и генераторы, Семинар 5, hw5-3
#
# -----------------
# Задача 3:
# Создайте функцию генератор чисел Фибоначчи

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def main():
    for number in fibonacci_generator(10):
        print(number)


if __name__ == "__main__":
    main()
