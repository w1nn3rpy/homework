names = open('people.txt', 'r')
summ = 0
try:
    for name in names:
        lenght = len(name) - 1
        if lenght < 3:
            raise BaseException('Ты сломал программу')
        else:
            summ += lenght
except BaseException:
    print('Программаа сломана')
else:
    print('Сумма символов =', summ)
