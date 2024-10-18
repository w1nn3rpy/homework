import json

import requests

"""
Внимательно изучите документацию этого API и напишите программу, 
которая выводит на экран (и в JSON-файл) информацию о пилотах легендарного истребителя X-wing.

Информация о корабле должна содержать следующие пункты:

название,
максимальная скорость,
класс,
список пилотов.

Внутри списка о каждом пилоте должна быть следующая информация:

имя,
рост,
вес,
родная планета,
ссылка на информацию о родной планете.
"""

x_wing_req = requests.get('https://www.swapi.tech/api/starships/12').json()
name = x_wing_req['result']['properties']['name']
max_speed = x_wing_req['result']['properties']['max_atmosphering_speed']
ship_class = x_wing_req['result']['properties']['starship_class']
pilots_links = x_wing_req['result']['properties']['pilots']

pilots = []
for pilot in pilots_links:
    req_pilots = requests.get(pilot).json()
    pilot_info = req_pilots['result']['properties']
    homeworld_data = requests.get(pilot_info['homeworld']).json()

    pilots.append({
        'name': req_pilots['result']['properties']['name'],
        'height': req_pilots['result']['properties']['height'],
        'mass': req_pilots['result']['properties']['mass'],
        'homeworld': homeworld_data['result']['properties']['name'],
        'homeworld_url': pilot_info['homeworld']
        })

result = {
    'ship_name': name,
    'max_speed': max_speed,
    'ship_class': ship_class,
    'pilots': pilots
}


with open('result.json', 'w') as file:
    json.dump(result, file, indent=4)

print(json.dumps(result, indent=4))
