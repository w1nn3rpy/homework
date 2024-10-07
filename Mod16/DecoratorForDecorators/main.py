from typing import Callable
import functools


def decorator_with_args_for_any_decorator(decorator):
    @functools.wraps(decorator)
    def wrapper(*d_args, **d_kwargs):
        def decorator_wrapper(func):
            return decorator(func, *d_args, **d_kwargs)
        return decorator_wrapper
    return wrapper


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    @functools.wraps(func)
    def wrapper(*f_args, **f_kwargs):
        print(f'Переданные арги и кварги в декоратор: {args}, {kwargs}')
        result = func(*f_args, **f_kwargs)
        return result
    return wrapper


@decorated_decorator('100', 'рублей', '200', 'друзей')
def decorated_func(text: str, num: int) -> None:
    print('Привет,', text, num)


decorated_func("Юзер", 101)
