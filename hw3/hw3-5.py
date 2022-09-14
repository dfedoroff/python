# Данные, функции и модули в Python, Семинар 3, hw3-5
#
# -----------------
# Задача 5:
# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
#
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def fibo(num):
    lst_pos = [1, 1]
    lst_neg = [0, 1]
    for i in range(num - 2):
        lst_pos.append(lst_pos[i] + lst_pos[i + 1])
    for i in range(num - 1):
        lst_neg.append(lst_neg[i] - lst_neg[i + 1])
    return lst_neg[::-1] + lst_pos

n = int(input('Введите число: '))
print(f'Cписок чисел Фибоначчи: {fibo(n)}')