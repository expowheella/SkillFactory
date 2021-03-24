class ParentClass:

    @classmethod
    def method(cls,arg):
        print(arg)

    @classmethod
    def call_original_method(cls):
        cls.method(5)

    def call_class_method(self):
        self.method(10)


class ChildClass(ParentClass):

    @classmethod
    def call_original_method(cls):
        cls.method(6)

ParentClass.method(10)
ParentClass.call_original_method()
v = ParentClass()
ParentClass.call_class_method(v)

ChildClass.call_original_method()
t = ChildClass()
ChildClass.method(80)
ChildClass.call_class_method(t)
