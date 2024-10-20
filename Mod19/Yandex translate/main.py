import requests
from decouple import config

API_KEY = config('API')
BASE_URL = 'https://dictionary.yandex.net/api/v1/dicservice.json'

def get_langs():
    response = requests.get(f'{BASE_URL}/getLangs', params={
        'key': API_KEY
    })
    return response

def lookup(lang, text, ui='ru'):
    response = requests.get(f'{BASE_URL}/lookup', params={
        'key': API_KEY,
        'lang': lang,
        'text': text,
        'ui': ui
    })
    return response

langs_response = get_langs()
if langs_response.status_code != 200:
    print('Не удалось получить список напралений перевода')
    exit(1)

langs = langs_response.json()
print('Выберите одно из направлений перевода')
print(langs)
while (lang := input('Введите направление: ')) not in langs:
    print('Такого направления нет')

text = input('Введите текст для перевода: ')

lookup_response = lookup(lang=lang, text=text)
if lookup_response.status_code != 200:
    print('Не удалось выполнить перевод: ', lookup_response.text)
    exit(1)

print(lookup_response.json())