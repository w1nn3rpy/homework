import os
import random


def search_file(path, file):
    result = list()
    for i_dir in os.listdir(path):
        full_path = os.path.join(path, i_dir)
        if i_dir == file:
            result.append(full_path)
        elif os.path.isdir(full_path):
            result += search_file(full_path, file)
    return result


search_path = '/Users/dmitriy/PycharmProjects/'
name = input('Введите имя файла для поиска: ')
list_of_paths = search_file(search_path, name)

if len(list_of_paths) > 0:

    file = open(random.choice(list_of_paths), 'r', encoding='utf-8')

    print('Содержимое файла', name)
    for i_line in file:
        print(i_line, end='')

    file.close()
else:
    print('Файл не найден!')
