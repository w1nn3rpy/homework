import re

text = r'How much \wwood+?, would a \wwood+?chuck \dwwood+, chuck if a \wwood+?,chuck could chuck \wwood?,'

r"""
Напишите программу, которая выводит список из всех упоминаний подстроки \wwood+?,
"""

pattern = re.compile(r'\\wwood\+\?,')
result = re.findall(pattern, text)
print('Список всех упоминаний шаблона:', result)