from contextlib import contextmanager


@contextmanager
def func(file, f_type):
    f = open(file, f_type, encoding='utf8')
    print(f.read())


func('input.txt', 'r') #
