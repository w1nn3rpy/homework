from typing import Callable
from time import sleep
from functools import wraps


def slowing(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs):
        sleep(2)
        return func(*args, **kwargs)
    return wrapper


@slowing
def some_dumb_func():
    print('Hello')


while True:
    some_dumb_func()