test = [x for x in range(10)]
print(test)
iterator = iter(test)
while True:
    try:
        print(iterator.__next__())
    except StopIteration:
        print('Итератор списка пуст.')
        break
