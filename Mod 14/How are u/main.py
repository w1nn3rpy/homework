from typing import Callable


def how_are_you(func: Callable) -> Callable:
    _ = input(' Как дела?')
    print('А у меня не очень. Ладно, держи свою функцию')
    return func


@how_are_you
def test():
    print('<Тут что-то происходит...>')


test()