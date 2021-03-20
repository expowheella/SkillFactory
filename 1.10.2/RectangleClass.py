class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def __str__(self):
        return f'Длина = {self.length}м,', f'Ширина = {self.width}м, ' \
                        f'\n\nПлощадь фигуры = {self.length * self.width}кв.м'
