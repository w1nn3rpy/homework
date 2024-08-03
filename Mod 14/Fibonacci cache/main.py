from typing import Callable
from functools import wraps


# def fibonacci():
#
#     fib_list = [0, 1]
#     while True:
#         fib_list.append(fib_list[-1] + fib_list[-2])
#         print(fib_list[-1], end=' ')
#
#
# fibonacci()

def cache(func):
    cache_dict = dict()

    @wraps(func)
    def wrapper(*args, **kwargs):
        if args in cache_dict:
            return cache_dict[args]

        result = func(*args, **kwargs)
        cache_dict[args] = result
        return result
    return wrapper


@cache
def fibonacci_recursive(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def gen_fibonacci(limit):
    n = 0
    while True:
        fib_num = fibonacci_recursive(n)
        if fib_num >= limit:
            break
        print(fib_num, end='')
        n += 1


gen_fibonacci(999999999999999999999999999999)
