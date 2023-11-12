class BankAccount:

    def __init__(self, balance, interest_rate, transactions):
        self.__balance = balance
        self.__interest_rate = interest_rate
        self.__transactions = []

    def deposit(self, amount):
        try:
            if amount > 0:
                self.__balance += amount
                self.__transactions.append(f'Транзакция выполнена. Пополнение счёта на сумму: {amount}. Ваш баланс: {self.__balance}\n')
            else:
                print(f'Ошибка. Пополнение должно быть не меньше 0. Ваше пополнение: {amount}\n')
        except ArithmeticError:
            print('Ошибка. Arithmetic Error')
        except TypeError:
            print('Ошибка. Type Error')

    def withdraw(self, amount):
        try:
            if self.__balance >= amount > 0:
                self.__balance -= amount
                self.__transactions.append(f'Транзакция выполнена. Снятие счёта на сумму: {amount}. Ваш баланс: {self.__balance}\n')
            elif self.__balance < amount:
                print('На счёте не достаточно денег')
            else:
                print(f'Ошибка. Пополнение должно быть не меньше 0. Ваше пополнение: {amount}\n')
        except ArithmeticError:
            print('Ошибка. Arithmetic Error')
        except TypeError:
            print('Ошибка. Type Error')

    def add_interest(self):
        try:
            i = self.__balance * self.__interest_rate
            self.__balance += i
            self.__transactions.append(f'Добавление процентов. Проценты:{i}\n')
        except ArithmeticError:
            print('Ошибка. Arithmetic Error')
        except TypeError:
            print('Ошибка. Type Error')

    def history(self, transactions):
        for tran in self.__transactions:
            print(f'Ваши транзакции: {tran}\n')

    def get_balance(self):
        print(f'Ваш баланс: {self.__balance}\n')


account = BankAccount(100000, 0.05, 0)
account.deposit(15000)
account.withdraw(7500)
account.add_interest()
account.history(0)