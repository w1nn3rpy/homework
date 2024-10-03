import functools
from typing import Callable


def repeat_decorator(_func=None, *, times=1):
    def repeat(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = None
            for _ in range(times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    if _func is None:
        return repeat
    return repeat(_func)


@repeat_decorator(times=5)
def do_times():
    print('Hello')


do_times()