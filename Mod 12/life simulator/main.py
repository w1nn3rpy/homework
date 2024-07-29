from random import randint


class KillError(Exception):
    pass


class DrunkError(Exception):
    pass


class CarCrashError(Exception):
    pass


class GluttonyError(Exception):
    pass


class DepressionError(Exception):
    pass


class Karma:
    """Класс счетчика кармы с приватным атрибутом, геттером и сеттером"""
    def __init__(self):
        self.__karma = 0

    def get_karma(self):
        return self.__karma

    def set_karma(self, num):
        self.__karma += num


def one_day():
    """
    Основной функционал программы
    1. Генерируется число от 1 до 10, при выпадении числа '1' (шанс 1 к 10) вызывается исключение
      1.1 Генерируется число от 1 до 5 для случайного выбора исключения
      1.2 Вызывается исключение в зависимости от числа.
    2. При выпадении числа отличного от '1' выводится сообщение 'День прошел удачно'
       и возвращается случайное число от 1 до 7 которое в будущем цикле будет прибавляться к карме
    """
    day_num = randint(1, 10)
    if day_num == 1:
        evil_number = randint(1, 5)
        if evil_number == 1:
            raise KillError('Вы случайно убили человека ^_^.')
        elif evil_number == 2:
            raise DrunkError('Вы напились... Всевышнему это не нравится.')
        elif evil_number == 3:
            raise CarCrashError('Вы попали в аварию. Следите за своей кармой.')
        elif evil_number == 4:
            raise GluttonyError('Вы объелись. Чревоугодие - грех.')
        elif evil_number == 5:
            raise DepressionError('Вы ушли в депрессию.')
    else:
        print('День прошел удачно')
        return randint(1, 7)


def main():
    """
    Цикл программы
    1. Открывается файл с логом исключений
    2. Инициализируется объект класса Karma
    3. Для быстрого доступа к счетчику инициализируется переменная для Геттера
    4. Запускается цикл.
    5. Результат цикла выводится на экран, а при вызове исключения еще и записывается в лог
    6. После завершения цикла файл с логом закрывается
    """
    log = open('karma.log', 'a', encoding='utf-8')
    karma = Karma()
    your_karma = karma.get_karma()
    while your_karma < 500:
        try:
            your_karma += one_day()
            print('Текущая карма - {}'.format(your_karma))
        except (KillError, DrunkError, CarCrashError, GluttonyError, DepressionError) as error:
            your_karma -= 15
            print(str(error), 'Карма минус пятнадцать.')
            log.write(str(error) + ' Карма минус пятнадцать. Ваша карма - {}\n'.format(your_karma))
    log.close()


main()
