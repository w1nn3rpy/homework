from collections.abc import Generator
class NumsQuad:
    """
    Класс-итератор выводящий квадраты чисел до указанного значения
    """
    def __init__(self, limit: int) -> None:
        self.limit = limit

    def __iter__(self):
        self.count = 0
        return self

    def __next__(self):
        if self.count < self.limit:
            self.count += 1
            return self.count ** 2
        raise StopIteration


quad = NumsQuad(10)
for num in quad:
    print(num)


def quad_generator(limit: int) -> Generator:
    """
    Функция-генеератор
    """
    for i_num in range(1, limit + 1):
        yield i_num ** 2


for quad in quad_generator(10):
    print(quad)


quads = (num ** 2 for num in range(1, 11))  # Генераторное выражение
for num in quads:
    print(num)
