def inf_gen():
    """
    Бесконечный генератор
    """
    count = 0
    while True:
        yield count
        count += 1


generator = inf_gen()

for num in generator:
    print(num)
