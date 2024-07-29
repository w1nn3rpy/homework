### Напишите программу, которая считывает из файла numbers.txt пары чисел,
# делит первое число на второе и выводит ответ на экран.
# Если первое число меньше второго, то программа выдаёт исключение DivisionError
# (нельзя делить меньшее на большее).


class DivisionError(Exception):
    pass


with (open('numbers.txt', 'r') as nums):
        for line in nums.readlines():
            try:
                splitline = line.split()
                num1, num2 = splitline[0], splitline[1]
                num1, num2 = int(num1), int(num2)
                print('Делим {} на {}'.format(num1, num2))
                if num1 < num2:
                    raise DivisionError('Нельзя делить большее на меньшее')
                else:
                    result = num1 / num2
                    print('Получилось {}'.format(round(result, 2)))
            except DivisionError as error:
                print(str(error))

