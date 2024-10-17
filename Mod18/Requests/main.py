import requests
import json

"""
Перейдите на сайт с API, посвящённый вселенной Star Wars.

После этого сгенерируйте реквест-ссылку на данные о человеке под номером 3 (people/3/). 

Затем напишите программу, которая парсит данные об этом человеке, 
изменяет его имя на ваше собственное и сохраняет результат в виде JSON-файла. 

Дополнительно: обратите внимание на значение ключа homeworld — там также хранится ссылка. 
В том же коде спарсите эту ссылку и посмотрите, что там.  

Примечание: API тоже пишут люди, а значит, время от времени его могут как-то менять и усовершенствовать, 
поэтому будьте внимательны: может быть, ссылка уже хранится в другом ключе.
"""

my_req = requests.get('https://www.swapi.tech/api/people/5')
data = json.loads(my_req.text)
data['result']['properties']['name'] = 'Dmitry'

with open('result.json', 'w') as file:
    json.dump(data, file, indent=4)

homeworld_link = data['result']['properties']['homeworld']
homeworld_req = requests.get(homeworld_link)
homeworld_data = json.loads(homeworld_req.text)
print(homeworld_data)

