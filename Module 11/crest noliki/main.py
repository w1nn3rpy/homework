class Board:  # класс поля
    def __init__(self):
        self.board = [Cell(i) for i in range(9)]

    def change_condition_cell(self, number):  # Проверка и смена состояния клетки
        if not self.board[number].is_busy:
            self.board[number].is_busy = True
            return True
        else:
            return False

    def check_finish(self):  # Проверка поля на победную линию
        flag = False         # Винооват, перебрал комбинации вручную
        board = self.board
        x = 'x'
        o = 'o'
        if board[0].symbol == x and board[1].symbol == x and board[2].symbol == x:
            flag = True
        elif board[0].symbol == x and board[3].symbol == x and board[6].symbol == x:
            flag = True
        elif board[0].symbol == x and board[4].symbol == x and board[8].symbol == x:
            flag = True
        elif board[1].symbol == x and board[4].symbol == x and board[7].symbol == x:
            flag = True
        elif board[2].symbol == x and board[4].symbol == x and board[6].symbol == x:
            flag = True
        elif board[2].symbol == x and board[5].symbol == x and board[8].symbol == x:
            flag = True
        elif board[3].symbol == x and board[4].symbol == x and board[5].symbol == x:
            flag = True
        elif board[6].symbol == x and board[7].symbol == x and board[8].symbol == x:
            flag = True

        if self.board[0].symbol == o and self.board[1].symbol == o and self.board[2].symbol == o:
            flag = True
        elif self.board[0].symbol == o and self.board[3].symbol == o and self.board[6].symbol == o:
            flag = True
        elif self.board[0].symbol == o and self.board[4].symbol == o and self.board[8].symbol == o:
            flag = True
        elif self.board[1].symbol == o and self.board[4].symbol == o and self.board[7].symbol == o:
            flag = True
        elif self.board[2].symbol == o and self.board[4].symbol == o and self.board[6].symbol == o:
            flag = True
        elif self.board[2].symbol == o and self.board[5].symbol == o and self.board[8].symbol == o:
            flag = True
        elif self.board[3].symbol == o and self.board[4].symbol == o and self.board[5].symbol == o:
            flag = True
        elif self.board[6].symbol == o and self.board[7].symbol == o and self.board[8].symbol == o:
            flag = True
        return flag


class Cell:  # класс клетки
    def __init__(self, num):
        self.is_busy = False  # Флаг занятости клетки
        self.number = num  # нумерация для инициализации через цикл
        self.symbol = ' '  # Изначально все клетки заняты пробелом


class Player:  # класс игрока
    def __init__(self):
        self.name = input('Введите имя: ')
        self.win = 0

    def do_step(self, cell):
        print('{} закрыл клетку {}'.format(self.name, cell))


class Game:  # класс управления ходом игры
    def __init__(self):
        self.state = None  # Флаг состояния игры
        self.players = [Player() for _ in range(2)]
        self.field = Board()
        self.who_step = 0  # Переменная по которой определяется чей сейчас ход
        self.step_count = 0  # переменная для подсчёта ходов для объявления ничьи

    def print_field(self):
        print('''
{}|{}|{}
-----
{}|{}|{}
-----
{}|{}|{}
'''.format(self.field.board[0].symbol, self.field.board[1].symbol, self.field.board[2].symbol,
           self.field.board[3].symbol, self.field.board[4].symbol, self.field.board[5].symbol,
           self.field.board[6].symbol, self.field.board[7].symbol, self.field.board[8].symbol))

    def one_step(self):
        self.print_field()
        try:
            offer = input('{}, введите номер клетки: '.format(self.players[self.who_step].name))
            if not offer.isdigit():
                raise ValueError('Некорректный ввод. Введите ЧИСЛО от 1 до 9')
            else:
                offer = int(offer)
            if not 0 <= offer - 1 <= 9:
                raise IndexError('Неверный номер клетки, введите число от 1 до 9')
            if self.who_step == 0:
                if self.field.change_condition_cell(offer - 1):
                    self.field.board[offer - 1].symbol = 'x'
                    self.players[0].do_step(offer)
                    self.step_count += 1

                    if self.field.check_finish():
                        print('{} победил!'.format(self.players[0].name))
                        self.players[0].win += 1
                        self.state = 'end'
                    else:
                        self.who_step = 1
                else:
                    print('Эта клетка уже занята')

            elif self.who_step == 1:
                if self.field.change_condition_cell(offer - 1):
                    self.field.board[offer - 1].symbol = 'o'
                    self.players[1].do_step(offer)
                    self.step_count += 1

                    if self.field.check_finish():
                        print('{} победил!'.format(self.players[1].name))
                        self.players[1].win += 1
                        self.state = 'end'
                    else:
                        self.who_step = 0
                else:
                    print('Эта клетка уже занята')
            else:
                raise ValueError('Некорректное значение. Введите число от 1 до 9.')
        except (IndexError, ValueError) as error:
            print(str(error))

    def start_new_game(self):
        self.field = Board()
        self.who_step = 0
        self.step_count = 0
        self.state = 'in-game'
        while not self.state == 'end':
            self.one_step()
            if not self.field.check_finish() and self.step_count == 9:  # Проверка на ничью
                print('Ничья! Победила дружба :)')
                self.state = 'end'
                break
        print('''Игрок {}: {} побед
Игрок {}: {} побед'''.format(self.players[0].name, self.players[0].win,
                             self.players[1].name, self.players[1].win))

    def main_start(self):

        while True:
            if self.state == 'end':
                try:
                    action = input('Хотите ли сыграть еще раз? Да/нет: ').lower()
                    if action == 'да':
                        self.start_new_game()
                    elif action == 'нет':
                        break
                    else:
                        raise ValueError('Введите "да" или "нет"')

                except ValueError as error:
                    print(str(error))
            else:
                self.start_new_game()


game = Game()
game.main_start()
