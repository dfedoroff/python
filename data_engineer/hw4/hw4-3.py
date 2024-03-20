# Погружение в Python, Часть 1. Функции, Семинар 4, hw4-3
#
# -----------------
# Задача 3:
# Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции - функции. Дополнительно сохраняйте
# все операции поступления и снятия средств в список.

class ATM:
    def __init__(self):
        self.balance = 0
        self.transaction_count = 0
        self.commission_rate = 0
        self.transaction_history = []

    def handle_transaction(self):
        operation = self.prompt_for_operation()
        if operation == 5:
            return False
        if operation in (1, 2) and (operation != 2 or self.balance != 0):
            self.process_transaction(operation)
        elif operation == 3:
            print(f"\nВаш баланс: {self.balance}")
        elif operation == 4:
            self.print_transaction_history()
        return True

    def prompt_for_operation(self):
        print(
            "\nВведите номер операции:\n"
            "1. Пополнение счета\n"
            "2. Снятие наличных\n"
            "3. Показать баланс\n"
            "4. История операций\n"
            "5. Выйти\n"
        )
        return int(input("Введите номер операции: "))

    def process_transaction(self, operation):
        if self.balance >= 5_000_000:
            self.commission_rate = 10
        amount = self.prompt_for_amount(operation)
        self.apply_transaction(operation, amount)

    def prompt_for_amount(self, operation):
        while True:
            amount = int(input("Введите сумму (кратную 50): "))
            if amount % 50 == 0:
                return amount
            else:
                print("Сумма должна быть кратной 50. Повторите попытку.")

    def apply_transaction(self, operation, amount):
        commission = 0.03 if self.transaction_count == 3 else 0 + self.commission_rate
        if operation == 1:  # Пополнение
            transaction_amount = amount - (amount * commission)
            self.balance += transaction_amount
            self.transaction_history.append(f"Пополнение +{transaction_amount}")
        elif operation == 2:  # Снятие
            if amount > self.balance:
                print("Ошибочная операция!")
                return
            fee = max(min(amount * (0.015 + commission), 600), 30)
            self.balance -= amount + fee
            self.transaction_history.append(f"Снятие средств -{amount}")
            self.transaction_history.append(f"Комиссия за снятие средств -{fee}")
        self.transaction_count += 1
