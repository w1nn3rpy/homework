class CountIterator:
    """
    Бесконечный итератор
    """
    def __init__(self):
        self.counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        self.counter += 1
        return self.counter -1


my_iter = CountIterator()

for i_elem in my_iter:

    print(i_elem)
