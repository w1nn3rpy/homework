from collections.abc import Generator
import os


def error_log_generator(path: str = '..') -> Generator:
    for root, dirs, files in os.walk(path):
        for file in files:
            if file:
                if file == 'error_strings.log':
                    continue
                path = os.path.join(root, file)
                with open(path, 'r', errors='replace') as opened_file:
                    count = 0
                    for line in opened_file:
                        count += 1
                        if 'ERROR' in line:
                            with open('error_strings.log', 'a') as log:
                                result = '{}|{}|Строка {}|"{}"'.format(path, file, count, line[:-1])
                                yield log.write(result + '\n')


for asd in error_log_generator('/Users/dmitriy/PycharmProjects/skillbox'):
    print(asd)
