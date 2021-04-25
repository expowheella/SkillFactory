class Node:
    def __init__(self, value=None, next_=None):
        self.value = value
        self.next = next_


class LinkedList:
    def __init__(self):
        self.first = None
        self.last = None

    def pushleft(self, value):
        if self.first is None:
            self.first = Node(value)
            self.last = self.first
        else:
            new_node = Node(value, self.first)
            self.first = new_node

    def popleft(self):
        if self.first is None: # если список пустой, возвращаем None
            return None
        elif self.first == self.last: # если список содержит только один элемент
            node = self.first # сохраняем его
            self.__init__() # очищаем
            return node # и возвращаем сохраненный элемент
        else:
            node = self.first # сохраняем первый элемент
            self.first = self.first.next # меняем указатель на первый элемент
            return node # возвращаем сохраненный
    def popright(self):
        if self.first is None: # если список пустой, возвращаем None
            return None
        elif self.first == self.last: # если список содержит только один элемент
            node = self.first # сохраняем его
            self.__init__() # очищаем
            return node # и возвращаем сохраненный элемент
        else:
            node = self.last # сохраняем последний
            pointer = self.first # создаем указатель
            while pointer.next is not node: # пока не найдем предпоследний
                pointer = pointer.next
            pointer.next = None # обнуляем указатели, чтобы
            self.last = pointer # предпоследний стал последним
            return node # возвращаем сохраненный
LL = LinkedList()

LL.pushleft(1)
LL.pushleft(2)
LL.pushleft(3)

print(LL)
