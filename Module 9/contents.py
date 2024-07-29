import os

abs_path = os.path.abspath(os.path.join('..', '..'))
print('Содержимое каталога', abs_path)
for i_dir in os.listdir(abs_path):
    print('   ', os.path.abspath(os.path.join(abs_path, i_dir)))
