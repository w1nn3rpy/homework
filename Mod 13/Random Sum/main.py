from random import uniform


class SumIterator:
    def __init__(self, limit):
        self.limit = limit
        self.index = 0
        self.value = uniform(0, 1)

    def __iter__(self):
        self.index = 0
        self.value = uniform(0, 1)
        return self

    def __next__(self):
        if self.index >= self.limit:
            raise StopIteration
        if self.index > 0:
            self.value += uniform(0, 1)
        self.index += 1
        return round(self.value, 2)


def test_iterator(limit):
    iterator = SumIterator(limit)
    print('Кол-во элементов: {}'.format(iterator.limit))
    print('Элементы итератоора:')
    for i_value in iterator:
        print(i_value)


test_iterator(5)
test_iterator(5)
print()

testing = SumIterator(5)

print('первый')
for val in testing:
    print(val)

print('второй')
for val in testing:
    print(val)