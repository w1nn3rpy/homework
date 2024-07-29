site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def search(key, obj):
    if key in obj:
        return obj[key]
    for sub_obj in obj.values():
        if isinstance(sub_obj, dict):
            res = search(key, sub_obj)
            if res:
                break
    else:
        res = None
    return res


form = input('Введите раздел для поиска: ')

value = search(form, site)

if value:
    print(value)
else:
    print('Такого ключа нет')