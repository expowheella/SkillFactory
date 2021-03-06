#  Sea Battle Game
from random import randint


# Exceptions
class BoardException(Exception):  # all exceptions
    pass


class BoardOutException(BoardException):  # special exception
    def __str__(self):
        return "Вы пытаетесь выстрелить за границу доски!"


class BoardUsedException(BoardException):  # special exception
    def __str__(self):
        return "Вы уже стреляли в эту клетку"


class BoardWrongShipException(BoardException):
    pass


#  bullet
class Dot:
    def __init__(self, x, y):  # ship = Dot(1,2) --> (dot, 1, 2)
        self.x = x  # a.x == 1
        self.y = y  # a.y == 1

    # checking if the arguments of the class objects (for ex. a and c) are equal to each other
    def __eq__(self, other):  # def __eq__(a, c):
        return self.x == other.x and self.y == other.y  # a.x == c.x and a.y == c.y     ## 1 ==1 and 1 == 1

    # this module returns a list of the objects were put on the board
    def __repr__(self):  # converts the object to a string in order to show it to user
        return f"{self.__class__.__name__}({self.x}, {self.y})"

#  ships
class Ship:
    def __init__(self, bow, length, orient):
        self.bow = bow
        self.length = length
        self.orient = orient  # shows how a ship is oriented on the board
        self.lives = 1

    # the dots represent ships on the board
    @property
    def dots(self):
        ship_dots = []

        # the bow (beginning) of the ship coordinates on the board
        for i in range(self.length):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.orient == 0:  # when orient == 0, a ship is oriented horizontally on the board
                cur_y += i  # fulfill the ship line step-by-step

            elif self.orient == 1:  # when orient == 1, a ship is oriented vertically on the board
                cur_x += i  # fulfill the ship line step-by-step

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots  # returning the list of dots on the board

    # checking if the shot dot belongs to a Ship
    def shot(self, ship):  # self = Ship(Dot(1, 2), 2, 1), ship = Dot(1, 2))
        return ship in self.dots  # Dot(1, 2) in [Dot(1, 2), Dot(1, 3)] --> True

# game board
class Board:
    def __init__(self, hidden=False, size=None):
        # the board parameters
        self.size = size
        self.hidden = hidden  # open or hide from eyes the competitor's board
        self.field = [["0"] * size for _ in range(size)]  # building a battlefield
        self.occupied = []  # a list of the occupied dots on the board

        # beaten ships quantity counter
        self.count = 0
        # a list of ships on the board
        self.ships = []

    # the game board interface
    def __str__(self):
        result = ""
        result += "  | 1 | 2 | 3 | 4 | 5 | 6 |"
        for i, row in enumerate(self.field, 1):
            result += f"\n{i} | " + " | ".join(row) + " |"

        # open or hide from eyes the competitor's board
        if self.hidden:
            result = result.replace("■", "0")
        return result

    # checking if the object in the field
    def out_of_field(self, object):
        # if x, y in range, return not True
        return not ((0 <= object.x < self.size) and (0 <= object.y < self.size))
        # return not (object.x in range(0, self.size)) and (object.y in range(0, self.size))

    def contour(self, object, verb=False):  # self = Board(), object = Ship(Dot(1, 2), 4, 0)
        area = [  # the area around the ship
            (-1, -1), (0, -1), (1, -1),
            (-1, 0), (0, 0), (1, 0),
            (-1, 1), (0, 1), (1, 1)
        ]
        for part_of_ship in object.dots:  # iterating the list of objects: [Dot(1, 2), Dot(1, 3)] ##  part_of_ship = Dot(1,2)
            for area_x, area_y in area:  # (area_x=-1, area_y=-1)
                # calculating coordinates around the ship
                area_around_ship = Dot(part_of_ship.x + area_x,
                                       part_of_ship.y + area_y)
                # if not False -> True and True
                if not (self.out_of_field(area_around_ship)) and area_around_ship not in self.occupied:
                    if verb:
                        self.field[area_around_ship.x][area_around_ship.y] = "."
                    self.occupied.append(area_around_ship)

    # putting ships on the battlefield
    def add_ship(self, object):  # (Ship(Dot(3, 1), 2, 0))
        for part_of_ship in object.dots:  # Dot(1, 2) in [Dot(1, 2), Dot(1, 3)]
            if self.out_of_field(part_of_ship) or part_of_ship in self.occupied:  # False
                raise BoardWrongShipException()

        for part_of_ship in object.dots:
            # print(part_of_ship)# Dot(1, 2) in [Dot(1, 2), Dot(1, 3)]
            try:
                self.field[part_of_ship.x][part_of_ship.y] = "■"  # replacing "0" with "■"
            except IndexError:
                continue
            else:
                self.occupied.append(part_of_ship)  # adding to the list of occupied dots o
                # n the field the coordinate field[1,2]

        self.ships.append(object)  # adding the ship into the list of ships
        self.contour(object)  # adding the object into the contour to show that the contur is occupied by the object

    def shot(self, object):
        # checking if the coordinates passed to the object in range (in the field)
        if self.out_of_field(object):
            raise BoardOutException()

        # checking if the object exists in the list of occupied dots
        if object in self.occupied:
            raise BoardUsedException()

        # if the object is not in the list of occupied dots, append it into the list
        self.occupied.append(object)

        # for each ship shown in the list of ships
        for ship in self.ships:

            # if the ship from user is an object: Dot(1, 2) in [Dot(1, 2), Dot(1, 3)] --> True
            if ship.shot(object):  # if ship in [Dot(1, 2), Dot(1, 3)]
                ship.lives -= 1
                self.field[object.x][object.y] = "X"
                if ship.lives == 0:
                    self.count += 1  # beaten ships quantity counter
                    self.contour(ship, verb=True)
                    print("Корабль уничтожен!")
                    return False  # no more ship parts in [Dot(1, 2), Dot(1, 3)]
                else:
                    print("Корабль ранен!")
                    return True  # there is still a rest of the ship

        # if there is no any ship in this coordinate
        self.field[object.x][object.y] = "."  # put "." on the board
        print("Мимо")
        return False

    # clearing a board from ships
    def begin(self):
        self.occupied = []

    def defeat(self):
        return self.count == len(self.ships)


class Player:
    def __init__(self, board, enemy):
        #  two boards: player's and the enemy's
        self.board = board
        self.enemy = enemy

    def ask(self):
        raise NotImplementedError()

    def move(self):
        while True:
            try:
                target = self.ask()  # request to input coordinates to shoot
                repeat = self.enemy.shot(target)
                return repeat
            except BoardException as e:
                print(e)


class AI(Player):
    def ask(self):
        d = Dot(randint(0, 5), randint(0, 5))  # the AI is shooting
        print(f'Ход компьютера: {d.x + 1} {d.y + 1}')  # to show user where AI has shot
        return d


class User(Player):
    def ask(self):
        while True:
            coords = input("Ваш ход: ").split()  # ['1', '2']

            if len(coords) != 2:
                print("Введите две координаты!")
                continue

            x, y = coords  # x = '1', y = '2'

            if not x.isdigit() or not y.isdigit():
                print("Нужно вводить числа, а не другие символы!")
                continue

            x, y = int(x), int(y)

            return Dot(x - 1, y - 1)


class Game:
    def __init__(self, size=6):
        self.size = size
        player_board = self.random_board()
        computer_board = self.random_board()
        computer_board.hidden = False

        self.ai = AI(computer_board, player_board)
        self.user = User(player_board, computer_board)


    def make_board(self):
        lengths = [3, 2, 2, 1, 1, 1, 1]  # ship lengths
        board = Board(size=self.size)
        attempts = 0
        for l in lengths:
            while True:
                attempts += 1
                if attempts > 2000:
                    return None
                ship = Ship(Dot(randint(0, self.size), randint(0, self.size)), l,
                            randint(0, 1))  # filling the board with ships randomly
                try:
                    board.add_ship(ship)
                    break
                except BoardWrongShipException:
                    pass
        board.begin()
        return board

    def random_board(self):
        board = None
        while board is None:
            board = self.make_board()
        return board

    def greet(self):
        print("--------------------")
        print("  Приветствуем Вас  ")
        print(" в игре Sea Battle ")
        print("--------------------")
        print(" формат ввода: x y  ")
        print("  x - номер строки  ")
        print("  y - номер столбца ")

# game flow
    def loop(self):
        num = 0
        while True:
            print("-"*20)
            print("Доска пользователя:")
            print(self.user.board)
            print("-" * 20)
            print("Доска компьютера:")
            print(self.ai.board)
            print("-" * 20)
            if num % 2 == 0:
                print('Ходит пользователь!')
                repeat = self.user.move()
            else:
                print('Ходит компьютер!')
                repeat = self.ai.move()
            if repeat:
                num -= 1

            if self.ai.board.defeat():
                print("-"*20)
                print("Пользователь выиграл!")
                break

            if self.user.board.defeat():
                print("-"*20)
                print("Пользователь выиграл!")
                break
            num +=1

            if self.ai.board.count == 7:
                print("-" * 20)


    def start(self):
        self.greet()
        self.loop()

g = Game()

g.start()
