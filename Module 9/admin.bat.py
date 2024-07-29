import os


def abs_path(file):
    path = os.path.abspath(file)
    return path


def relative_path(file):
    path = os.path.join('..', '..', file)
    return path


file = 'admin.bat'

print(abs_path(file))
print(relative_path(file))
