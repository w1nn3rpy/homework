from typing import Callable

PLUGINS = dict()


def add_plugin_decorator(func: Callable) -> Callable:
    PLUGINS[func.__name__] = func
    return func


@add_plugin_decorator
def say_hello(name: str) -> str:
    return f'Hello, {name}'


@add_plugin_decorator
def say_goodbye(name: str) -> str:
    return f'Goodbye, {name}'


print(PLUGINS)
print(say_hello('Max'))
print(say_goodbye('Max'))
print(PLUGINS)
