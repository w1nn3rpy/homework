def check(data):

    if type(data) is list:
        is_type = 'список'
        is_mute = 'Изменяемый'

    elif type(data) is dict:
        is_type = 'словарь'
        is_mute = 'Изменяемый'

    elif type(data) is set:
        is_type = 'множество'
        is_mute = 'Изменяемый'

    elif type(data) is str:
        is_type = 'строка'
        is_mute = 'Неизменяемый'

    elif type(data) is int:
        is_type = 'число'
        is_mute = 'Неизменяемый'

    elif type(data) is tuple:
        is_type = 'кортеж'
        is_mute = 'Неизменяемый'

    elif type(data) is bool:
        is_type = 'булево значение'
        is_mute = 'Неизменяемый'

    elif type(data) is float:
        is_type = 'число с плавающей точкой'
        is_mute = 'Неизменяемый'

    elif data is None:
        is_type = 'Пустое значение'
        is_mute = 'Неизменяемый'

    is_id = id(data)

    return is_type, is_mute, is_id


data = None

i_type, mute, i_id = check(data)

print('Тип данных:', i_type)
print(mute)
print('id объекта:', i_id)
