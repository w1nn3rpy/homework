import os

path = '/Users/dmitriy/PycharmProjects/skillbox/Module 9/'

print('Абсолютный путь:', path)

if os.path.exists(path):
    if os.path.isdir(path):
        print('Это директория')

    if os.path.isfile(path):
        print('Это файл')
        print('Размер файла:', os.path.getsize(path), 'байт')

    if os.path.islink(path):
        print('Это ссылка')

else:
    print('Указанного пути не существует')