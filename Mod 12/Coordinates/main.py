class Dot:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def set_y(self, value):
        if isinstance(value, int):
            self.__y = value

    def set_x(self, value):
        if isinstance(value, int):
            self.__x = value

    def get_y(self):
        return self.__y

    def get_x(self):
        return self.__x

    def __str__(self):
        return 'Точка X: {}\nТочка Y: {}'.format(self.get_x(), self.get_y())


a, b = Dot(1, 90), Dot()
print(a)
print(b)
b.set_x(99)
b.set_y(-5)
print(b)
