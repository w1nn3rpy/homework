from typing import Callable, Dict

routes: Dict[str, Callable] = {}


def callback(path: str) -> Callable:
    def decorator(func: Callable) -> Callable:
        routes[path] = func
        return func
    return decorator


class App:
    def get(self, path: str) -> Callable | None:
        return routes.get(path, None)


@callback('//')
def example() -> str:
    print('Пример функции возвращающей ответ')
    return 'OK'


app = App()
route = app.get('//')

if route:
    response = route()
    print(f'Ответ: {response}')
else:
    print('Такого пути нет')