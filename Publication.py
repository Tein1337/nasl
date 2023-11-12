class Publication:

    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def display(self):
        print(f'Название: {self.title}')
        print(f'Автор: {self.author}')
        print(f'Год: {self.year}')


class Book(Publication):
    def __init__(self, title, author, year, isbn):
        super().__init__(title, author, year)
        self.isbn = isbn

    def display(self):
        super().display()
        print(f'ISBN: {self.isbn}')


class Magazine(Publication):
    def __init__(self, title, author, year, issue_number):
        super().__init__(title, author, year)
        self.issue_number = issue_number

    def display(self):
        super().display()
        print(f'Номер журнала: {self.issue_number}')


def info(obj):
    obj.display()

p = Publication('Название1', 'Автор1', 2000)
b = Book('Название2', 'Автор2', 2100, 10)
n = Magazine('Название3', 'Автор4', 21000, 100)
list = []
list.append(p)
list.append(b)
list.append(n)
for i in list:
    info(i)
    print()


