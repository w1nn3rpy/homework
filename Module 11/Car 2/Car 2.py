from random import randint


class Toyota:
    color = 'red'
    price = 1000000
    max_speed = 200
    current_speed = 0

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


toyota_1 = Toyota()
toyota_1.current_speed = randint(0, 200)

toyota_2 = Toyota()
toyota_2.current_speed = randint(0, 200)

toyota_3 = Toyota()
toyota_3.current_speed = randint(0, 200)

toyota_3.info()

toyota_3.set_current_speed(400)
toyota_3.info()