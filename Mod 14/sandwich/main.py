def decorator(func):
    print('</----------\\>')
    func()
    print('<\\______/>')


@decorator
def sandwich():
    print('#помидоры#')
    print('--ветчина--')
    print('~салат~')
