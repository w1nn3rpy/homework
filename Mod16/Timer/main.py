from contextlib import contextmanager
from _collections_abc import Iterator
import time


@contextmanager
def timer() -> Iterator:
    start = time.time()
    try:
        yield
    except Exception as ex:
        print(f'Ошибка: {ex}')
    finally:
        print(time.time() - start)


with timer() as t1:
    print('Таймер 1')
    val1 = 100 * 100 ** 1000000

with timer() as t2:
    print('Таймер 2')
    val2 = 200 * 200 ** 1000000

with timer() as t3:
    print('Таймер 3')
    val3 = 300 * 300 ** 1000000
