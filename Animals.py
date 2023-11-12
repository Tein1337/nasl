class Animal:

    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def voice(self):
        print(f'{self.name} подает голос\n')

    def move(self):
        print(f'{self.name} дергает хвостом\n')


class Dog(Animal):

    def __init__(self, name, species, legs, breed):
        super().__init__(name, species, legs)
        self.breed = breed

    def bark(self):
        print(f'{self.species} {self.name} лает\n')


class Bird(Animal):

    def __init__(self, name, species, legs, wingspan):
        super().__init__(name, species, legs)
        self.wingspan = wingspan

    def fly(self):
        print(f'{self.species} {self.name} летает\n')


dog = Dog("Геральт", "Доберман", 4, 'rfdssae')
bird = Bird("Вася", "Попугай", 2, 'dasddsa')
dog.voice()
bird.voice()
dog.move()
bird.move()
dog.bark()
bird.fly()