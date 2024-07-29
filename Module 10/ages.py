names = ['Алина', 'Максим', 'Дмитрий', 'Андрей', 'Сергей',
         'Алексей', 'Александр', 'Вася', 'Петя', 'Оксана']

try:
    with open('ages.txt', 'r') as ages:
        res = dict()
        ages_list = [age for age in ages]
        for i_index in range(len(ages_list)):
            res[names[i_index]] = ages_list[i_index]

    with open('result.txt', 'w') as result:
        for name, age in res.items():
            result.write(name + ' ' + age)
except FileExistsError:
    print('Файл уже существует')
except IsADirectoryError:
    print('Выбрана директория. Требуется файл')
except (TypeError, ValueError):
    print('Ошибка типа либо значения файла.')

ages.close()
result.close()
