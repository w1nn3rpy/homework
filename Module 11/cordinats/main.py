class Dot:
    x = 0
    y = 0

    counter = 0

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.counter += 1

    def print_info(self):
        print('Точка X: {}\nТочка Y: {}'.format(self.x, self.y))


new = Dot(3)
new.print_info()