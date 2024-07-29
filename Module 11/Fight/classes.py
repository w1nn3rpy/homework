from random import randint


class Warrior:

    def __init__(self):
        self.hp = 100
        self.damage = 20


class Fight:

    def __init__(self, warrior1, warrior2):
        while warrior1.hp > 0 and warrior2.hp > 0:

            atack = randint(1, 2)

            if atack == 1:
                warrior2.hp -= warrior1.damage
                print('Боец 1 атаковал и нанес {} урона'.format(warrior1.damage))

            else:
                warrior1.hp -= warrior2.damage
                print('Боец 2 атаковал и нанес {} урона'.format(warrior2.damage))
            self.print_status(warrior1, warrior2)

        if warrior1.hp > 0:
            print('Воин 1 одержал победу')
        else:
            print('Воин 2 одержал победу')

    def print_status(self, warrior1, warrior2):
        print('Боец 1 имеет {} очков здоровья\nБоец 2 имеет {} очков здоровья'.format(warrior1.hp, warrior2.hp))