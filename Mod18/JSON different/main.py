import json
from idlelib.iomenu import encoding

"""
Найдите различия между двумя JSON-файлами. Если различающиеся параметры входят в diff_list,
выведите различие. Иными словами, вам нужно отловить изменение определённых параметров
и вывести значение: что изменилось и на что. Набор ключей в обоих файлах идентичный, различаются лишь значения.

Напишите программу, которая:

1.загружает данные из двух предложенных JSON-файлов (находятся в репозитории);
2.выполняет сравнение параметров, указанных в diff_list;
3.формирует результат в виде словаря;
4.записывает словарь в JSON-файл с названием result.json.

Исходные данные

Файлы:

json_old.json,
json_new.json.
Список параметров для отслеживания (можно сформировать инпутом или ввести вручную):

diff_list = [‘services’, ‘staff’, ‘datetime’]

Формат итогового словаря с результатом:

Словарь {параметр: новое_значение, ….}
"""

diff_list = ['services', 'staff', 'datetime']

with (open('json_old.json', 'r', encoding='utf-8') as json_old,
      open('json_new.json', 'r', encoding='utf-8') as json_new):
    data_old = json.loads(json_old.read())
    data_new = json.loads(json_new.read())



result = {}

def findkey(data, key):
    if isinstance(data, dict):
        if key in data:
            return data[key]
        for sub_key, sub_value in data.items():
            if isinstance(sub_value, dict):
                found = findkey(sub_value, key)
                if found is not None:
                    return found
    elif isinstance(data, list):
        for item in data:
            found = findkey(item, key)
            if found is not None:
                return found

def compare_value(key, old, new):
    if old != new:
        result[key] = new

for key in diff_list:
    old_value = findkey(data_old, key)
    new_value = findkey(data_new, key)
    compare_value(key, old_value, new_value)

print(result)

with open('result.json', 'w') as res:
    json.dump(result, res, indent=4)

