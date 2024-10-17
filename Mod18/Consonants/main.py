import re

text = 'Even if they are djinns, I will get djinns that can outdjinn them.'

"""
Используя регулярные выражения, напишите программу, которая выводит два списка:

Первый содержит все слова, которые начинаются на гласную букву латинского алфавита 
(в этот раз слово может состоять и из одной буквы, например I).
Второй содержит слова, которые начинаются на любой символ, кроме гласных букв латинского алфавита.
"""

first_pattern = r'\b[aeiouAEIOU]\w*'
first_list = re.findall(first_pattern, text)
print(first_list)

second_pattern = r'\b[^ aeiouAEIOU]\w+'
second_list = re.findall(second_pattern, text)
print(second_list)
