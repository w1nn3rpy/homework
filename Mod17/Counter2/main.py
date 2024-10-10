###  Вариант с локальной переменной  ###

# class Counter:
#     def __init__(self, func):
#         self.count = 0
#         self.func = func
#
#     def __call__(self, *args, **kwargs):
#         self.count += 1
#         print(f'Функция {self.func.__name__} вызвана {self.count} раза')
#         result = self.func(*args, **kwargs)
#         return result
#
#
# @Counter
# def test_1():
#     print('test')
#
# test_1()
# test_1()

###  Вариант с глобальной переменной  ###

count = 0

class Counter:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        global count
        count += 1
        print(f'Функция {self.func.__name__} вызвана {count} раза')
        result = self.func(*args, **kwargs)
        return result


@Counter
def test_1():
    print('test')

test_1()
test_1()