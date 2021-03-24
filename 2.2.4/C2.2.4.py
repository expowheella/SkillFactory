class SquareFactory:
    @staticmethod
    def sq_side(arg):
        return arg


class Square(SquareFactory):
    def get_result(self, arg):
        return SquareFactory.sq_side(arg)


r = Square()  # r - это экземпляр класса Square

# два варианта передачи аргумента при вызове одного и того же метода:
print(Square.get_result(r, 6))  # вызов метода get_result класса Square с указанием экземпляра класса
print(r.get_result(6))  # то же самое, только по-другому записано
