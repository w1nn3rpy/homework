def quicksort(lst):

    point = lst[-1]
    high = list()
    mid = list()
    low = list()

    for i_elem in lst:
        if i_elem > point:
            high.append(i_elem)
        elif i_elem < point:
            low.append(i_elem)
        else:
            mid.append(i_elem)

    if high:
        high = quicksort(high)
    if low:
        low = quicksort(low)

    res = low + mid + high

    return res


print(quicksort([5, 8, 9, 4, 2, 9, 1, 8]))
