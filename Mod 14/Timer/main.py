import time


def timer(func, *args, **kwargs):
    start = time.time()
    result = func(*args, **kwargs)
    end = time.time()
    run_time = round(end - start, 4)
    print('Функция работала {} секунд'.format(run_time))
    return result


def quad_sum(num):
    num = num
    result = 0
    for _ in range(num + 1):
        result += sum([x ** 2 for x in range(100)])
    return result


print(timer(quad_sum, 500000))
