# Погружение в Python, Часть 1. Основы Python, Семинар 1, Домашнее задание

Каталоги и файлы             | Описание
-----------------------------|-----------------------------------------------------
`/python/data_engineer/hw1/` | Каталог файлов домашнего задания
`/hw1/.gitignore`            | Файл для исключения из индексации Git файлов и папок
`/hw1/README.md`             | Условия задач
`/hw1/hw1-1.py`              | Решение задачи 1
`/hw1/hw1-2.py`              | Решение задачи 2
`/hw1/hw1-3.py`              | Решение задачи 3


### Задача 1:

Треугольник существует только тогда, когда сумма любых двух его сторон больше третьей. Дано `a`, `b`, `c` - стороны предполагаемого треугольника. Требуется сравнить длину каждого отрезка-стороны с суммой двух других. Если хотя бы в одном случае отрезок окажется больше суммы двух других, то треугольника с такими сторонами не существует. Отдельно сообщить является ли треугольник разносторонним, равнобедренным или равносторонним.

## Задача 2:

Напишите код, который запрашивает число и сообщает является ли оно простым или составным. Используйте правило для проверки: "Число является простым, если делится нацело только на единицу и на себя". Сделайте ограничение на ввод отрицательных чисел и чисел больше `100 000`.

## Задача 3:

Программа загадывает число от `0` до `1000`. Необходимо угадать число за `10` попыток. Программа должна подсказывать "больше" или "меньше" после каждой попытки. Для генерации случайного числа используйте код:
`from random import randintnum = randint(LOWER_LIMIT, UPPER_LIMIT)`


