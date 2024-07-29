class Parrent:

    def __init__(self):
        self.name = input('Введите имя: ')
        self.age = int(input('Введите возраст: '))
        self.my_child = input('Введите имя своего ребенка: ')

    def print_info(self):
        print('Меня зовут {}, мне {} лет, моего ребенка зовут {}'.format(self.name, self.age, self.my_child))

    def calm(self, child):
        print('{}: {}, не плачь, я люблю тебя'.format(self.name, child.name))
        child.calm_status = 1
        child.is_calm()

    def feed(self, child):
        print('{}: {}, кушай, мой хороший'.format(self.name, child.name))
        child.hungry = 0
        child.is_hungry()


class Child:
    def __init__(self, parrent):
        self.name = parrent.my_child
        try:
            self.age = int(input('Введите возраст ребенка: '))
            if parrent.age - self.age < 16:
                raise ValueError('Родитель должен быть старше ребенка как минимум на 16 лет')
        except ValueError as e:
            print(str(e))
            Child.__init__(self, parrent)

        self.calm_status = 0
        self.hungry = 1

    def is_calm(self):
        if self.calm_status == 0:
            print('{} плачет, его нужно успокоить'.format(self.name))
        else:
            print('{} спокоен'.format(self.name))

    def is_hungry(self):
        if self.hungry == 1:
            print('{} смотрит на живот, его нужно покормить'.format(self.name))
        else:
            print('{} сыт'.format(self.name))

    def print_status(self):
        print('Проверяем, как там {}'.format(self.name))
        self.is_calm()
        self.is_hungry()


mom = Parrent()
child = Child(mom)

actions = '''1 - Информация о родителе
2 - Состояние ребенка
3 - Успокоить ребенка
4 - Покормить ребенка
0 - Выйти с программы'''

print(actions)

while True:
    action = int(input('Введите номер действия: '))

    if action == 0:
        break
    elif action == 1:
        mom.print_info()
    elif action == 2:
        child.print_status()
    elif action == 3:
        mom.calm(child)
    elif action == 4:
        mom.feed(child)
    else:
        print(actions)