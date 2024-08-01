from typing import Callable


def decorator(func: Callable) -> None:
    print('</----------\\>')
    func()
    print('<\\______/>')


@decorator
def sandwich() -> None:
    print('#помидоры#')
    print('--ветчина--')
    print('~салат~')
