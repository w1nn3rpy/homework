def func_1(x):
    return x + 10


def func_2(func, *args):
    num = func(*args)
    result = num ** 2
    return result


print(func_2(func_1, 9))