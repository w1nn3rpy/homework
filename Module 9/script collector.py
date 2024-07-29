import os


def fileopen(path_to):
    if os.path.isfile(path_to):
        temp = open(path_to)
        data = temp.read()
        temp.close()
        return data
    else:
        dirs = os.listdir(path_to)
        for dirr in dirs:
            if dirr:
                return fileopen(os.path.abspath(os.path.join(path_to, dirr)))


names = os.listdir()

scripts = open('scripts.txt', 'a')

mypath = os.path.abspath('../Module 9')

for name in names:
    scripts.write(fileopen(os.path.join(mypath, name)) + '\n' + ('*' * 40) + '\n')

scripts.close()
