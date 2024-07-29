class Monitor:
    name = 'Samsung'
    matrix = 'VA'
    res = 'WQHD'
    freq = 60


class Headphones:
    name = 'Sony'
    sensitivity = 108
    microphone = True


monitors = [Monitor() for _ in range(4)]
for index, value in enumerate([60, 144, 70, 60]):
    monitors[index].freq = value

headphones = [Headphones() for _ in range(3)]
headphones[2].microphone = False

