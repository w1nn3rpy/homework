from random import randint

count = 0

with open('out_file.txt', 'w') as out_file:
    try:
        while count < 777:
            fatal = randint(1, 13)
            if fatal == 10:
                raise StopIteration

            else:
                num = int(input('Введите число: '))
                count += num
                out_file.write(str(num) + '\n')
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
    except StopIteration:
        print('Вас постигла неудача :(')