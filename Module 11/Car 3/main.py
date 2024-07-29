class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    current_speed = 0

    def __init__(self, colour='black', amount=1000000, mx_speed=200, cur_speed=0):
        self.color = colour
        self.price = amount
        self.max_speed = mx_speed
        self.current_speed = cur_speed

    def info(self):
        print('Color: {}\nPrice: {}\nMax speed: {}\nCurrent speed: {}'.format(
            self.color, self.price, self.max_speed, self.current_speed
            )
        )

    def set_current_speed(self, speed):
        if speed > self.max_speed:
            print('Car cant ride faster than max speed')
            self.current_speed = self.max_speed
        else:
            self.current_speed = speed
        print('Set new current speed: {}'.format(self.current_speed))


car = Toyota('blue', 500000, 210, 100)

car.info()