from typing import Callable
from functools import wraps


class Counter:
    count = 0


def counter(func: Callable) -> Callable:

    @wraps(func)
    def wrapper(*args, **kwargs):
        Counter.count += 1
        print(f'Функция {func.__name__} была вызвана {Counter.count} раз')
        return func(*args, **kwargs)

    return wrapper


@counter
def check(num: int) -> int:
    return 2 + num


print(check(2))
print(check(5))
print(check(3))


def counter(func: Callable):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"Количество вызовов функции {func.__name__}: {wrapper.calls}")
        return func(*args, **kwargs)

    wrapper.calls = 0
    return wrapper


@counter
def example_function() -> str:
    return "Функция вызвана"


print(example_function())
print(example_function())
print(example_function())
