# Простая учетная система банка
# Задача : Определите класс Account, имитирующий банковский счет. Класс должен включать атрибуты для хранения идентификатора владельца, баланса счета и методы для депозита (пополнения) и снятия средств, если на счету достаточно средств.
# Цели научиться : Работа с числовыми данными, выполнение условий (например, проверка баланса перед снятием денег), изменение и отслеживание состояния объекта.


class Account:
    def __init__(self, owner_id, balance=0):
        self.owner_id = owner_id
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Баланс после пополнения: {self.balance}")

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            print(f"Баланс после снятия: {self.balance}")
        else:
            print("Недостаточно средств для снятия.")

    def get_balance(self):
        return self.balance


account = Account("123", 1000)

print(f"Текущий баланс: {account.get_balance()}")
account.withdraw(500)
account.deposit(200)
account.withdraw(2000)
print(f"Баланс: {account.get_balance()}")
