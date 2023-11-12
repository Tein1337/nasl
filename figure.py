class Figure:

    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color


    def draw(self):
        print(f'Рисуем фигуру цветом {self.color} и шириной {self.width}')


class Line(Figure):

    def draw(self):
        print(f'Рисуем линию цветом {self.color} и шириной {self.width}')

    def del_line(self):
        print('Линия удалена')


class Rect(Figure):

    def __init__(self, coords, width, color, right):
        super().__init__(coords, width, color)
        self.right = right

    def draw(self):
        print(f'Рисуем прямоугольник цветом {self.color} и шириной {self.width}. Прямоугольник {self.right}')


class Ellips(Figure):

    def draw(self):
        print(f'Рисуем эллипс цветом {self.color} и шириной {self.width}')



f = Figure([1,2,3,4,5,6,7,8], 2, 'black')
f.draw()
l = Line([1,1,5,6], 3, 'red')
l.draw()
l.del_line()
e = Ellips([1,2,3,4], 3, 'green')
e.draw()
r = Rect([1,8,6,2], 6, 'blue', 'неправильный')
r.draw()