# Погружение в Python, Часть 1. Итераторы и генераторы, Семинар 5, hw5-2
#
# -----------------
# Задача 2:
# Напишите однострочный генератор словаря, который принимает на вход три
# списка одинаковой длины: имена str, ставка int, премия str с указанием
# процентов вида 10.25%. В результате получаем словарь с именем в качестве
# ключа и суммой премии в качестве значения. Сумма рассчитывается как ставка
# умноженная на процент премии

def calculate_bonus_sum(names, wages, bonus_percents):
    return {
        name: wage + (wage * float(bonus_percent.rstrip("%")) / 100)
        for name, wage, bonus_percent in zip(names, wages, bonus_percents)
    }


def print_bonus_sums(bonus_sums):
    for name, total in bonus_sums.items():
        print(f"Имя сотрудника: {name} \t зарплата сотрудника с учётом премии: {total}")


def main():
    names = ["Алексей", "Наталья", "Любовь"]
    wages = [35_000, 40_000, 300_000]
    bonus_percents = ["23%", "32.5%", "100%"]
    bonus_sums = calculate_bonus_sum(names, wages, bonus_percents)
    print_bonus_sums(bonus_sums)


if __name__ == "__main__":
    main()
