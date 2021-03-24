class Dog:

    def __init__(self, number):
        self.number = number

    @property
    def dog_number(self):
        return self.number

    @dog_number.setter
    def dog_number(self, value):
        self.number = value
        return self.number


Bob = Dog(5)  # 5
print(Bob.dog_number)
Bob.dog_number = 50
print(Bob.dog_number)  # 50
