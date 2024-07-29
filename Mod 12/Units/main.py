class Unit:
    def __init__(self, hp):
        self.name = None
        self.__hp = hp

    def get_damage(self, damage):
        if self.__hp > 0:
            self.__hp -= damage
            if self.__hp <= 0:
                print('Юнит {} получил {} урона и погиб.'.format(self.name, damage))
            else:
                print('Юнит {} получил {} урона. Осталось {} единиц здоровья.'.format(self.name, damage, self.__hp))


class Solider(Unit):
    def __init__(self, hp):
        super().__init__(hp)
        self.hp = hp
        self.name = 'Солдат'


class Innocent(Unit):
    def __init__(self, hp):
        super().__init__(hp)
        self.name = 'Гражданин'

    def get_damage(self, damage):
        super().get_damage(damage * 2)


solider = Solider(hp=100)
innocent = Innocent(hp=100)

solider.get_damage(50)
innocent.get_damage(40)
solider.get_damage(20)
innocent.get_damage(20)
