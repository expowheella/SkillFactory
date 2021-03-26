
#  ships
class Ship:
    def __init__(self, bow, l, orient):
        self.bow = bow
        self.l = l
        self.orient = orient  # shows how a ship is oriented on the board
        self.lives = 1

    # the dots represent ships on the board
    def dots(self):
        ship_dots = []

        # the bow (beginning) of the ship coordinates on the board
        for i in range(self.l):
            cur_x = self.bow.x
            cur_y = self.bow.y

            if self.orient == 0:  # when orient == 0, a ship is oriented horizontally on the board
                cur_x += i        # fulfill the ship line step-by-step

            elif self.orient == 1:  # when orient == 1, a ship is oriented vertically on the board
                cur_y += i          # fulfill the ship line step-by-step

            ship_dots.append(Dot(cur_x, cur_y))

        return ship_dots  # returning the list of dots on the board

craiser = Ship(Dot(1, 2), 4, 1)
print(craiser.dots())
