
def do_twice(func):
    def wrapped(*args, **kwargs):
        func(*args, **kwargs)
        func(*args, **kwargs)
        return
    return wrapped


@do_twice
def greeting(name):
    print('Привет, {name}!'.format(name=name))


greeting('Tom')