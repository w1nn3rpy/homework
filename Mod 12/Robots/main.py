class Robot:
    def __init__(self, model, weapon=None):
        self.model = model

    def __str__(self):
        return self.operate()

    def operate(self):
        pass


class RobotCleaner(Robot):
    def __init__(self, model):
        super().__init__(model)
        self.__bag = 0

    def operate(self):
        self.__bag += 1
        return 'Я - робот {}, навожу порядок. Заполненность мешка для мусора: {}'.format(
            self.model, str(self.__bag))

    def set_bag_fullness(self):
        self.__bag += 1
        print('О, мусор. Я убрал.')


class RobotDefender(Robot):
    def __init__(self, model, weapon=None):
        super().__init__(model, weapon)
        self.__weapon = weapon

    def operate(self):
        if self.__weapon:
            return 'Я - робот {}. Моё оружие - {}. Я охраняю базу.'.format(self.model, self.__weapon)
        else:
            return 'Я - робот {}.'.format(self.model)


class RobotSubmarine(Robot):
    def __init__(self, model, weapon):
        super().__init__(model)
        self.__weapon = weapon

    def operate(self):
        return 'Я - робот {}. Моё оружие - {}. Я охраняю базу под водой'.format(
            self.model, self.__weapon)


cleaner = RobotCleaner('Пылесос')
defender = RobotDefender('Защитник', 'Лазер')
submarine = RobotSubmarine('Субмарина', 'Торпеды')

print(cleaner)
print(defender)
print(submarine)

print(cleaner.operate())

print(cleaner.operate())

print(defender.operate())
