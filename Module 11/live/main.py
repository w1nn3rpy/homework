from random import randint


class House:

    def __init__(self):
        self.food = 50
        self.money = 0


class Human:

    alive = True

    def __init__(self):
        self.name = input('Введите имя: ')
        self.hungry = 50
        self.house = House()
        print('{}: Я родился!'.format(self.name))

    def eat(self):
        self.house.food -= 10
        self.hungry += 10
        print('Вы съели бутерброд. Еда - 10, сытость + 10')
        print('Осталось {} единиц еды из 100. Уровень сытости {}'.format(self.house.food, self.hungry))

    def work(self):
        self.hungry -= 10
        if self.hungry <= 0:
            print('Вы умерли от голода на работе')
            self.alive = False
        else:
            self.house.money += 25
            print('Вы сходили на работу и заработали 25 деняк, но проголодались, сытость - 10')
            print('Накопления: {} деняк. Уровень сытости {}'.format(self.house.money, self.hungry))

    def play(self):
        self.hungry -= 5
        if self.hungry <= 0:
            self.alive = False
            print('Вы умерли от голода во время игры')
        else:
            print('Вы решили сыграть. Сытость - 5')
            print('Уровень сытости {}'.format(self.hungry))

    def shopping(self):
        self.house.money -= 10
        self.house.food += 15
        print('Вы сходили в магазин и купили продуктов. Деньги - 10, еда + 15')
        print('Осталось {} деняк. Еды в холодильнике {}/100'.format(self.house.food, self.hungry))

    def alive_one_day(self):
        print('Пытаемся прожить еще один день :)')
        cube_num = randint(1, 6)
        print('Вы бросили кубик и выпало число {}'.format(cube_num))
        if self.hungry < 20:
            print('Ваша сытость меньше 20. Вы обязаны поесть.')
            self.eat()
        elif self.house.food < 10:
            print('Вы заметили, что еды в холодильнике осталось меньше 10/100')
            self.shopping()
        elif self.house.money < 50:
            print('Да уж. Осталось совсем мало деняк, пора на работу.')
            self.work()
        elif cube_num == 1:
            print('Вы обязаны подчиниться воле кубика и пойти на работу :)')
            self.work()
        elif cube_num == 2:
            print('Вы обязаны подчиниться воле кубика и сладко покушац)))')
            self.eat()
        else:
            print('Ну делать нечего. Время поиграть')
            self.play()


alex = Human()

act = '''1 - Прожить еще один день.
2 - Поесть
3 - Работать
4 - Сходить в магазин
5 - Играть
6 - Вывести статистику

0 - Завершить программу'''

print(act)


while alex.alive is True:

    action = int(input('Введите действие: '))
    if action == 1:
        alex.alive_one_day()
    elif action == 2:
        alex.eat()
    elif action == 3:
        alex.work()
    elif action == 4:
        alex.shopping()
    elif action == 5:
        alex.play()
    elif action == 6:
        print('''
В доме осталось {} еды
{} cыт на {}%
Запас - {} деняк'''.format(
            alex.house.food, alex.name,
            alex.hungry, alex.house.money))
    else:
        print('Неверная команда')
        print(act)