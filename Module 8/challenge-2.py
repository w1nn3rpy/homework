def match_num(num):
    if num != 0:
        match_num(num - 1)
        print(num)


num = int(input('Введите число: '))

match_num(num)
