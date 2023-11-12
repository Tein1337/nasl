class Shape:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def describe(self):
        print(f'Это геометрическая фигура, цвет - {self.color}.')


class Circle(Shape):

    def __init__(self, name, color, radius):
        super().__init__(name, color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def describe(self):
        print(f'Это геометрическая фигура, цвет - {self.color}.')
        print(f'Это окружность. Радиус - {self.radius} см, цвет - {self.color}')


class Rectangle(Shape):

    def __init__(self, name, color, length, width):
        super().__init__(name, color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def describe(self):
        print(f'Это геометрическая фигура, цвет - {self.color}.')
        print(f'Это {self.color} {self.name}. Длина - {self.length} см, ширина - {self.width} см.')


class Triangle(Shape):

    def __init__(self, name, color, base, height):
        super().__init__(name, color)
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

    def describe(self):
        print(f'Это геометрическая фигура, цвет - {self.color}.')
        print(f'Это {self.color} {self.name} с онснованием {self.base} см и высотой {self.height} см.')


circle = Circle('окружность', 'красный', 5)
rectangle = Rectangle('прямоугольник', 'синий', 3, 4)
triangle = Triangle('треугльник', 'фиолетовый', 6, 8)

circle.describe()
rectangle.describe()
triangle.describe()

print(f"Площадь треугольника {triangle.area()}, окружности {circle.area()}, прямоугольника {rectangle.area()} см.")