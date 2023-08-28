# Задание №6
# Изменяем класс прямоугольника.
# Заменяем пару декораторов проверяющих длину и ширину
# на дескриптор с валидацией размера.

class DimensionValidator:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if value <= 0:
            raise ValueError("должно быть больше нуля")
        instance.__dict__[self.name] = value

class Rectangle:
    height = DimensionValidator('_Rectangle__height')
    width = DimensionValidator('_Rectangle__width')

    def __init__(self, height: int, width=None):
        self.height = height
        if width:
            self.width = width
        else:
            self.width = height

    def get_perimeter(self):
        return 2 * (self.height + self.width)

    def get_area(self):
        return self.width * self.height

    def __str__(self):
        return f'прямоугольник ({self.width}х{self.height}), S= {self.get_area()}'

    def __repr__(self):
        return f'размеры:({self.width}х{self.height}), S= {self.get_area()}'

if __name__ == "__main__":
    rect = Rectangle(2, 5)
    rect.width = 3

    print(rect)
