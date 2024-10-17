import re

"""
В России для транспорта применяются регистрационные знаки нескольких видов.

Общее в них то, что они состоят из цифр и букв. Причём используются только 12 букв кириллицы, 
имеющих графические аналоги в латинском алфавите: А, В, Е, К, М, Н, О, Р, С, Т, У и Х.

У частных легковых автомобилей номера — это буква, три цифры, две буквы, затем две или три цифры с кодом региона.

У такси — две буквы, три цифры, затем две или три цифры с кодом региона.

Напишите программу, которая в перечне номеров находит номера частных автомобилей и номера такси.
"""

reg_list = 'А578ВЕ777 ОР233787 К901МН666 СТ46599 СНИ2929П777 666АМР666'

private_numbers = re.findall(r'\b[АВЕКМНОРСТУХ]\d{3}[АВЕКМНОРСТУХ]+\d{2,3}', reg_list)
taxi_numbers = re.findall(r'\b[АВЕКМНОРСТУХ]{2}\d{3}\d{2,3}', reg_list)
print(f'Список частных номеров: {private_numbers}')
print(f'Список номеров такси: {taxi_numbers}')