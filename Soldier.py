class Soldier:

    def __init__(self, name, rank, service_number ):
        self.name = name
        self.__rank = rank
        self.__service_number = service_number

    def get_rank(self):
        print(self.__rank)

    def y_service_number(self):
        try:
            if self.__service_number == 12345:
                print('Солдат на своем месте')
            else:
                print('Солдат не на своем месте')
        except TypeError:
            print('Ошибка. Type Error')

    def promote(self):
        print(f'Солдат: {self.name} повышен с {self.__rank} до Ефрейтор')

    def demote(self):
        try:
            if self.__rank == "рядовой":
                print('Ниже некуда')
            else:
                print(f'Солдат: {self.name} понижен с {self.__rank} до Курсанта')
        except TypeError:
            print('Ошибка. Type Error')


soldier1 = Soldier("Петр Тестов", "рядовой", "228")
soldier1.get_rank()
soldier1.promote()
soldier1.demote()