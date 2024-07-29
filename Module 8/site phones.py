import copy


def search(key1, key2, newstring1, newstring2, obj):
    if key1 in obj:
        obj[key1] = newstring1
    if key2 in obj:
        obj[key2] = newstring2
    for sub_obj in obj.values():
        if isinstance(sub_obj, dict):
            res = search(key1, key2, newstring1, newstring2, sub_obj)
            if res:
                break
    else:
        res = None
    return res


site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

list_of_sites = list()

site_count = int(input('Введите количество сайтов: '))

for i_site in range(site_count):
    name = input('Введите название продукта для нового сайта: ')
    list_of_sites.append({name: copy.deepcopy(site)})
    search('title',
           'h2',
           'Куплю/продам {} недорого'.format(name),
           'У нас самая низкая цена на {}'.format(name),
           list_of_sites[i_site])
    for sites in list_of_sites:
        print(sites)
