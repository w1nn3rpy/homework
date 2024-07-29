def search(obj, target, deep_in=None):
    if target in obj:
        return obj[target]

    if deep_in is None or deep_in <= 0:
        deep_in = None

    for sub_obj in obj.values():
        if isinstance(sub_obj, dict):
            if deep_in is None or deep_in == 1:
                return None
            res = search(sub_obj, target, None if deep_in is None else deep_in - 1)
            if res is not None:
                return res
    return None


def ask(question, retries=3):
    while retries > 0:
        answer = input(question).lower()
        if answer == 'y':
            return int(input('Введите глубину вложенности: '))
        elif answer == 'n':
            return None
        else:
            retries -= 1
            print('Введите Y/N')

    print('Закончились попытки ввода. Глубина не установлена.')
    return None


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

key = input('Введите ключ для поиска: ')

deep = ask('Хотите ли вы задать глубину вложенности для поиска? Y/N: ')

result = search(site, key, deep)

if result is None:
    print('Ключ не найден')
else:
    print('Значение ключа', result)
