import requests
import re
from bs4 import BeautifulSoup


url = input('Вставьте ссылку на страницу: ')
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    formatted_html = soup.prettify()
    with open('index.html', 'w') as file:
        file.write(formatted_html)
        print('html файл страницы сохранён')

else:
    print('Нет ответа от сервера')

text = response.text
h3_pattern = re.compile(r'<h3>(.*?)</h3>', re.IGNORECASE | re.DOTALL) # Поиск тегов
title_pattern = re.compile(r'>(.*?)<') # Поиск содержимого тегов

tags = re.findall(h3_pattern, text)
result = []

for tag in tags:
    result.append(*re.findall(title_pattern, tag))

print(result)

