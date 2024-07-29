from math import sqrt


def calculate(num):
    try:
        if num.isalpha():
            raise TypeError('Вы ввели букву. Введите число.')

        if num.isdigit():
            if float(num) < 0:
                raise ValueError('Вы ввели отрицатеельное число. Введите число больше нуля.')

        if not num.isdigit():
            raise TypeError('Вы ввели хуй пойми что, не букву и не цифру. Исправляйте.')

        else:
            result = round(sqrt(int(num)), 3)
            print(result)

    except (ValueError, TypeError) as error:
        print(str(error))


number = input('Введите число для вычисления квадратного корня: ')

calculate(number)
