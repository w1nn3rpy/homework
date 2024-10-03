import functools
import time


def delay_decorator(_func=None, *, sleep=1):
    def delay(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            time.sleep(sleep)
            result = func(*args, **kwargs)
            return result
        return wrapper
    if _func is None:
        return delay
    return delay(_func)


@delay_decorator
def print_hello():
    print('hello')
    print('hello')
    print('hello')


print_hello()
