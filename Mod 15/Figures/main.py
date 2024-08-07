from abc import ABC, abstractmethod


class Figure(ABC):
    def __init__(self, x: int, y: int, length: int, width: int) -> None:
        self._x = x
        self._y = y
        self._length = length
        self._width = width

    def move(self, x: int, y: int) -> str:
        self._x = x
        self._y = y
        return f'{self.__class__.__name__}: New coordinates: x={self._x}, y={self._y}'


class ResizableMixIn:
    def resize(self, length: int, width: int) -> str:
        self._length = length
        self._width = width
        return f'{self.__class__.__name__}: New size: {int(self._length)}x{int(self._width)}'


class Square(Figure, ResizableMixIn):
    def __init__(self, x: int, y: int, size) -> None:
        super().__init__(x, y, size, size)


class Rectangle(Figure, ResizableMixIn):
    pass


kvadrat = Square(10, 15, 40)
print(kvadrat.resize(2, 2))
print(kvadrat.resize(4, 4))
print(kvadrat.move(22, 40))

prmglnk = Rectangle(5, 15, 20, 40)
print(prmglnk.resize(25, 50))