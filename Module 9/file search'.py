import os


def search_file(path, file):
    result = list()
    for i_dir in os.listdir(path):
        full_path = os.path.join(path, i_dir)
        if i_dir == file:
            result.append(full_path)
        elif os.path.isdir(full_path):
            result += search_file(full_path, file)
    return result


path = '/Users/dmitriy/PycharmProjects/'

name = 'new palindrom.py'

for i_path in search_file(path, name):
    print(i_path)