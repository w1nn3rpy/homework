def sum(*args):
    res = 0
    for i_elem in args:
        if isinstance(i_elem, int):
            res += i_elem
        else:
            for i_key, i_value in enumerate(i_elem):
                res += sum(i_value)
    return res


print(sum([[1, 2, [3]], [1], 3]))
print(sum(1, 2, 3, 4, 5))
