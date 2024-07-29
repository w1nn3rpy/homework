def open_list(x_list):
    res = list()
    for i_elem in x_list:
        if isinstance(i_elem, int):
            res.append(i_elem)
        else:
            res += open_list(i_elem)
    return res


nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]], [[11, 12, 13], [14, 15], [16, 17, 18]]]

print(open_list(nice_list))
