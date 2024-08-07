
class Robot:
    def __init__(self, model: str) -> None:
        self._model = model

    def operate(self) -> None:
        print(f'Я - робот {self._model}')


class CanFly(Robot):
    def __init__(self, model: str, height: int, speed: int) -> None:
        super().__init__(model)
        self._height = height
        self._speed = speed

    def take_off(self) -> None:
        print(f'Робот {self._model}: Набираю высоту')
        self._height += 10
        print(f'Робот {self._model}: Высота - {self._height}м.')

    def fly(self) -> None:
        print(f'Робот {self._model}: Набираю скорость')
        self._speed += 10
        print(f'Робот {self._model}: Скорость - {self._speed}км/ч')

    def to_land(self) -> None:
        print(f'Робот {self._model}: Приземляюсь')
        self._height = 0
        print(f'Робот {self._model}: Высота - {self._height}м.')


class FlyScoutRobot(CanFly):
    def __init__(self, model: str, height: int, speed: int) -> None:
        super().__init__(model, height, speed)

    def operate(self) -> None:
        print(f'Робот {self._model}: Веду разведку с воздуха.')


class FlySoldierRobot(CanFly):
    def __init__(self, model: str, height: int, speed: int) -> None:
        super().__init__(model, height, speed)

    def operate(self) -> None:
        print(f'Робот {self._model}: Защищаю военный объект с воздуха')


scout = FlyScoutRobot('Разведчик', 100, 50)
soldier = FlySoldierRobot('Истребитель', 200, 100)

scout.operate()
soldier.operate()
scout.take_off()
soldier.fly()
scout.fly()
scout.to_land()
soldier.to_land()