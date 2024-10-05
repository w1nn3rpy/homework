import functools
from typing import Callable


user_permissions = ['user_1']


def check_permission(rights: str) -> Callable:
    def do_func(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs) -> str:
            try:
                if rights == user_permissions[0]:
                    result = func(*args, **kwargs)
                    return result
                else:
                    raise PermissionError('PermissionError')
            except PermissionError as ex:
                print(f'{ex}: У пользователя недостаточно прав, чтобы выполнить функцию {func.__name__}')
        return wrapper
    return do_func


@check_permission('admin')
def delete_site():
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    print('Добавляем комментарий')


delete_site()
add_comment()
