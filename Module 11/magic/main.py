class Water:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Steam.answer
        elif isinstance(other, Earth):
            return Dirt.answer
        elif isinstance(other, Air):
            return Storm.answer
        else:
            return None

    def __init__(self):
        print('Это вода!')


class Earth:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lava.answer
        elif isinstance(other, Water):
            return Dirt.answer
        elif isinstance(other, Air):
            return Dust.answer
        else:
            return None

    def __init__(self):
        print('Это земля!')


class Fire:
    def __add__(self, other):
        if isinstance(other, Water):
            return Steam.answer
        elif isinstance(other, Earth):
            return Lava.answer
        elif isinstance(other, Air):
            return Lighting.answer
        else:
            return None

    def __init__(self):
        print('Это огонь!')


class Air:
    def __add__(self, other):
        if isinstance(other, Fire):
            return Lighting.answer
        elif isinstance(other, Earth):
            return Dust.answer
        elif isinstance(other, Water):
            return Storm.answer
        else:
            return None

    def __init__(self):
        print('Это воздух!')


class Steam:
    answer = 'Вы сложили огонь и воду и получили лаву!'


class Storm:
    answer = 'Вы сложили воду и воздух и получили шторм!'


class Dirt:
    answer = 'Вы сложили воду и землю и получили грязь!'


class Lighting:
    answer = 'Вы сложили огонь и воздух и получили молнию!'


class Dust:
    answer = 'Вы сложили воздух и землю и получили пыль!'


class Lava:
    answer = 'Вы сложили огонь и землю и получили лаву!'


water = Water()
air = Air()
fire = Fire()
earth = Earth()

print(water + earth)
print(fire + air)