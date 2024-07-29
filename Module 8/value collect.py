def test(num, lst=[1, 2, 3]):
    lst = lst or []
    if not lst:
        lst = []
    lst.append(num)
    print(lst)


test(5)
test(10)
test(15)