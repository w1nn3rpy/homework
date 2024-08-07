from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self, colour, speed):
        self._colour = colour
        self._speed = speed
        self._place = 0

    def drive(self):
        self._place += self._speed
        print(f'{self._colour} {self.__class__.__name__}: За час вы проехали {self._speed}км, '
              f'сейчас вы за {self._place}км от города')

    def signal(self):
        print(f'{self._colour} {self.__class__.__name__}: Бип-бип')


class MusicMixIn(ABC):
    def play_music(self):
        print(f'{self.__class__.__name__}: Потому, что есть оЛёшка у тебя')


class Auto(Transport):
    def __init__(self, colour, speed):
        super().__init__(colour, speed)


class Boat(Transport):
    def __init__(self, colour, speed):
        super().__init__(colour, speed)


class Amphibian(Transport, MusicMixIn):
    def __init__(self, colour, speed):
        super().__init__(colour, speed)


auto = Auto('red', 100)

auto.drive()
auto.drive()
boat = Boat('blue', 30)
boat.drive()
boat.drive()
auto.drive()
auto.signal()
boat.signal()

amph = Amphibian('Green', 25)
amph.signal()
amph.drive()
amph.play_music()