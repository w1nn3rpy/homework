import os
from contextlib import contextmanager


@contextmanager
def in_dir(path):
    home = os.path.abspath(os.curdir)
    print(f'Домашняя папка: {home}')
    checkdir = os.path.abspath(path)
    try:
        print(f'Установили папку для сканироования: {checkdir}')
        os.chdir(checkdir)
        print(f'Перешли в {checkdir}')
        yield
    except Exception as ex:
        print(f'Ошибка: {ex}')
    finally:
        print(f'Переходим из:\n{checkdir} в {home}')
        os.chdir(home)
        print(f'Текущая директория: {os.path.abspath(os.path.curdir)}')


with in_dir('/Users/dmitriy/'):
    print(os.listdir())
