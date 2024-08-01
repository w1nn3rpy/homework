import datetime
from typing import Callable
from functools import wraps
from datetime import *


def logging(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print('Функция: ', func.__name__)
            print('Документация: ', func.__doc__)
            return func(*args, **kwargs)
        except Exception as e:
            error_msg = f"{datetime.now().strftime(
                '%Y-%m-%d %H:%M:%S')} 'Название функции: {func.__name__}\nОшибка: {str(e)}\n"

            with open('function_errors.log', 'a') as log:
                log.write(error_msg)

    return wrapper


@logging
def some_dumb_func():
    print('hello')


@logging
def one_more_dumb_func():
    """
    Пытаемся получить ошибку
    """
    print(some_dumb_func)


some_dumb_func()
one_more_dumb_func(222)