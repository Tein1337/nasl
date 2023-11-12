class Employee:

    def __init__(self, name, age, salary, bonus):
        self.__name = name
        self.__age = age
        self.__salary = salary
        self.__bonus = bonus

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_salary(self):
        return self.__salary

    def set_bonus(self, bonus):
        self.__bonus = bonus

    def get_bonus(self, bonus):
        return self.__bonus

    def get_total_salary(self):
        sum = self.__bonus + self.__salary
        return f'Общая зарплата сотрудника: {sum}'


e = Employee("Антонина Петровна", 35, 90000, 0)

e.set_bonus(100)

print("Имя:", e.get_name())
print("Возраст:", e.get_age())
print("Зарплата:", e.get_salary())
print("Бонус:", e.get_bonus(0))
print("Итого начислено:", e.get_total_salary())