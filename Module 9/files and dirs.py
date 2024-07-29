import os


def search(start, point):
    for i_dir in os.listdir(start):
        newpath = os.path.join(start, i_dir)
        if i_dir == point:
            result = newpath
            return result
        elif os.path.isdir(newpath):
            result = search(newpath, point)
            if result:
                return result


def math(path):
    dirs = 0
    files = 0
    size = 0
    for i_dir in os.listdir(path):
        newpath = os.path.join(path, i_dir)

        if os.path.isfile(newpath):
            files += 1
            size += os.path.getsize(newpath)

        elif os.path.isdir(newpath):
            sub_dir, sub_files, sub_size = math(newpath)
            dirs += sub_dir + 1
            files += sub_files
            size += sub_size

    return dirs, files, size


start = '/Users/dmitriy/PycharmProjects'

path_from = search(start, 'skillbox')

dirs, files, size = math(path_from)

print(path_from)
print('Размер каталоога (в Кбайтах):', size / 1024)
print('Количество подкаталогов:', dirs)
print('Количество файлов:', files)
