import re

"""
Для макетов веб-страниц часто используется какой-нибудь текст-рыба — это условный, 
нередко бессмысленный текст-заполнитель. Пусть дан следующий сгенерированный текст:
"""

text = """ Lorem ipsum dolor sit amet, consectetuer adipiscing elit. 
Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes,
nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. 
Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate 
"""

"""
Напишите программу, которая обрабатывает этот текст и выводит список слов, состоящих ровно из четырёх букв.
"""


result = re.findall(r'\b\w{4}\b', text)
print(result)