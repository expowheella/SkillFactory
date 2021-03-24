class Square:
    _a = None  # submit an empty parameter for using it to pass the properties

    def __init__(self, arg):
        # defining a side of the square
        self.side_a = arg

    @property
    def side_a(self):
        return self._a

    @side_a.setter
    def side_a(self, value):
        if value > 0:
            self._a = value
        else:
            self._a = 0

    @property
    def get_square(self):
        return self.side_a ** 2


square_calculation = Square(arg=2)
print(square_calculation.side_a)
print(square_calculation.get_square)


