class SquareFactory:
    @staticmethod
    def sq_side(arg):
        return arg


class Square(SquareFactory):
    def get_result(self, arg):
        return SquareFactory.sq_side(arg)


r = Square()
print(r.get_result(6))
