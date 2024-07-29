import time
from typing import Callable, Any


def timer(func: Callable) -> Callable:
    def wrapped(*args, **kwargs) -> Any:
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        run_time = round(end - start, 4)
        print('Функция работала {} секунд'.format(run_time))
        return result
    return wrapped


@timer
def quad_sum(num: int) -> float | int:
    num = num
    result = 0
    for _ in range(num + 1):
        result += sum([x ** 2 for x in range(100)])
    return result


print(quad_sum(100000))
