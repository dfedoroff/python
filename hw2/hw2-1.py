# Знакомство с языком Python, Семинар 2, hw2-1
#
# -----------------
# Задача 1:
# Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.
# 
# Пример:
# - 0,56 -> 11

n = float(input('Введите вещественное число: '))
num = str(n).split('.')
sum = 0
for i in num:
    for j in i:
        sum += int(j)
print(f'Сумма всех цифр вещественного числа = {sum}')
