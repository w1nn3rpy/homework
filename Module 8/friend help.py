def create_dict(data, temp=None):
    if isinstance(data, dict):
        return data

    elif isinstance(data, (int, float, str)):
        temp = temp or dict()
        if not temp:
            temp = dict()
            temp[data] = data
        return temp


def data_preparation(old_list):
    new_list = []

    for i_element in old_list:
        new_elem = create_dict(i_element)
        if new_elem:
            new_list.append(new_elem)

    return new_list


data = ['sad', {'sds': 23}, {43}, [12, 42, 1], 23.23]

data = data_preparation(data)

print(data)

