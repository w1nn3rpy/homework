

from collections.abc import Generator
import os


def gen_files_path(__target: str, __start_dir: str = '/') -> Generator[str, None, None]:
    for root, dirs, files in os.walk(__start_dir):
        if __target in dirs:
            target_dir_files = os.path.join(root, __target)
            for dir_root, _, dir_files in os.walk(target_dir_files):
                for file in dir_files:
                    yield os.path.join(dir_root, file)


if __name__ == '__main__':
    target = 'Mod 13'
    start_dir = '/Users/dmitriy/PycharmProjects/'
    for file_path in gen_files_path(target, start_dir):
        print(file_path)
