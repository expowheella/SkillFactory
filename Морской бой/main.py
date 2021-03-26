#  Sea Battle Game

# Exceptions
class BoardException(Exception):  # all exceptions
    pass


class BoardOutException(BoardException):  # special exception
    def __str__(self):
        return "Вы пытаетесь выстрелить в доску!"


class BoardUsedException(BoardException):  # special exception
    def __str__(self):
        return "Вы уже стреляли в эту клетку"


class BoardWrongShipException(BoardException):
    pass


#  bullet
class Dot:
    def __init__(self, x, y):  # def __init__(a, 1, 1):
        self.x = x  # a.x == 1
        self.y = y  # a.y == 1

    # checking if the arguments of the class objects (for ex. a and c) are equal to each other
    def __eq__(self, other):  # def __eq__(a, c):
        return self.x == other.x and self.y == other.y  # a.x == c.x and a.y == c.y     ## 1 ==1 and 1 == 1

    # this module returns the object dots on the board
    def __repr__(self):
        return f"Dot({self.x}, {self.y})"


# a = Dot(1, 1)
# b = Dot(3, 2)
# c = Dot(1, 1)

# checking if the object a is equal to the object c
# print(a.x == c.x and a.y == c.y)  # (1 == 1 and 1 == 1)

# printing a list of the class objects
# print([a, b, c])

# checking if a is in the list aa
# aa = [Dot(1, 1), Dot(3, 5), Dot(10, 11), Dot(1, 1), Dot(2, 1)]
# print(a in aa)
#
# # checking how many objects a are in the list
# print(aa.count(a))


#  ships
class Ship:
    def __init__(self, bow, length, orient):
        self.bow = bow
        self.length = length
        self.orient = orient  # shows how a ship is oriented on the board
        self.lives = 1

    # the dots represent ships on the board
    def dots(self):
        ship_dots = []

        # the bow (beginning) of the ship coordinates on the board
        for i in range(self.length):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.orient == 0:  # when orient == 0, a ship is oriented horizontally on the board
                cur_x += i        # fulfill the ship line step-by-step

            elif self.orient == 1:  # when orient == 1, a ship is oriented vertically on the board
                cur_y += i          # fulfill the ship line step-by-step

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots  # returning the list of dots on the board

craiser = Ship(Dot(1, 2), 1, 1)
print(craiser.dots())