def a():
    print("a")


def b():
    print("b")


def c():
    print("c")


dict = {'a': a, 'b': b, 'c': c}

dict['a']()
dict['b']()
dict['c']()

class A:
    def __init__(self, b):
        self.b=b

c=A(1)

setattr(c, "b", 10)

print(c.b)

from sub import a

if __name__ == '__main__':
    print("a")