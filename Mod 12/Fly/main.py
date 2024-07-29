class CanFly:
    def __init__(self):
        self.height = 0
        self.speed = 0

    def __takeoff(self):
        pass

    def __fly(self):
        pass

    def __to_land(self):
        pass

    def print_info(self):
        print('Текущая высота: {} м., текущая скорость: {}км/ч'.format(self.height, self.speed))


class Butterfly(CanFly):
    def __str__(self):
        return 'Это очень красивая бабочка ^_^'

    def takeoff(self):
        self.height = 1
        print('Бабочка затрепетала крыльями...')
        self.print_info()

    def fly(self):
        self.speed = 0.5
        print('Бабочка куда-то полетела')
        self.print_info()


class Rocket(CanFly):
    def __str__(self):
        return 'Это большая ракета несущая огромный боезаряд.'

    def takeoff(self):
        self.height = 500
        self.speed = 1000
        print('Ракета запущена, скорость и высоота набраны.')
        self.print_info()

    def __boom(self):
        print('Произошел взрыв\nРакета попала в цель')

    def to_land(self):
        self.height = 0
        self.print_info()
        self.__boom()


bubby = Butterfly()
x22 = Rocket()

print(bubby)
print(x22)
bubby.takeoff()
bubby.fly()

x22.takeoff()
x22.to_land()

bubby.print_info()
x22.print_info()
