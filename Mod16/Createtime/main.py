import functools
import datetime


def createtime(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        timenow = datetime.datetime.now(datetime.UTC).isoformat('|', 'seconds')
        print(f'Время создания инстанса класса: {timenow}')
        return instance
    return wrapper


def all_methods(cls):
    @functools.wraps(cls)
    def wrapper(*args, **kwargs):
        instance = cls(*args, **kwargs)
        my_methods = []
        for i_method in dir(cls):
            if i_method.startswith('__') is False:
                my_methods.append(i_method)
        print(f'Список функций класса {cls.__name__}:', *my_methods)
        return instance
    return wrapper


@all_methods
@createtime
class Math:

    def num_sum(self, num1, num2):
        print(num1 + num2)

    def sqrt_nums(self, num1, num2):
        print(num1 ** num2)


mathing = Math()
mathing.num_sum(50, 200)
mathing.sqrt_nums(50, 20)

newmath = Math()