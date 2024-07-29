def inf_gen():
    """
    Бесконечный генератор простых чисел
    """
    count = 1
    while True:
        count += 1
        prime = True
        for i in range(2, (int(count ** 0.5)) + 1):
            if count % i == 0:
                prime = False
                break
        if prime:
            yield count


generator = inf_gen()

for num in generator:
    print(num)
