# Знакомство с языком Python, Семинар 2, hw2-4
#
# -----------------
# Задача 4:
# Задайте список из N элементов, заполненных числами из
# промежутка [-N, N]. Найдите произведение элементов на
# указанных пользователем через пробел позициях.

import random
n = int(input('Введите число: '))
list = []
for i in range(0, n):
    list.append(random.randint(-n, n))
print(f'Список из {n} элементов: {list}')
pos_num = input((f'Введите через пробел максимум {n} позиции элементов: ')).split(" ")
pos = [int(i) for i in pos_num]
if len(pos) < n + 1:
    prod = 1
    for i in range(len(pos)):
        prod *= (list[pos[i]])
    print(f'Произведение выбранных элементов = {prod}')