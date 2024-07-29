import os
from collections.abc import Generator


def string_counter(path: str = '..') -> Generator[str]:
    for root, dirs, files in os.walk(path):
        for file in files:
            if file:
                path = os.path.join(root, file)
                with open(path, 'r') as opened_file:
                    count = 0
                    for line in opened_file:
                        if line and not line.startswith('#') and not line.startswith('\n'):
                            count += 1
                yield 'В файле {} каталога {} - {} строк'.format(file, path, count)


if __name__ == '__main__':
    for result in string_counter():
        print(result)
