import functools
from datetime import datetime


def for_all_methods(decorator):
    @functools.wraps(decorator)
    def decorate(cls):
        for i_method_name in dir(cls):
            if i_method_name.startswith('__') is False:
                cur_method = getattr(cls, i_method_name)
                decorated_method = decorator(cur_method)
                setattr(cls, i_method_name, decorated_method)
        return cls
    return decorate


def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        log_time = f'{datetime.now().isoformat('|', 'seconds')} - Запуск метода "{func.__name__}"'
        log_doc = f'Документация: {func.__doc__}'
        getargs = ', '.join([str(arg) for arg in args])
        log_args = f'Аргументы функции: {getargs}'
        print(log_time)
        print(log_args)
        if func.__doc__ is not None:
            print(log_doc)
        return result
    return wrapper


@for_all_methods(logger)
class MyClass:
    def method_1(self):
        """
        Выводит 'Hello'
        """
        print('Hello')

    def method_2(self):
        """
        Выводит 'How are u?'
        """
        print('How are u?')

    def method_3(self):
        print('Bye bye')


mc = MyClass()
mc.method_1()
mc.method_2()
mc.method_3()