from typing import List
from functools import reduce

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

"""
Напишите код, который создаёт три новых списка. Вот их содержимое:

1. Каждое число из списка floats возводится в третью степень и округляется до трёх знаков после запятой.
2. Из списка names берутся только имена минимум из пяти букв.
3. Из списка numbers берётся произведение всех чисел.
"""

cube_float: List[float] = [round(i, 3) for i in map(lambda x: (x ** 3), floats)]
five_chars_names: List[str]= [name for name in names if len(name) >= 5]
multiply_numbers: List[int] = [reduce(lambda x, y: x * y, numbers)]

print(f'1. {cube_float}')
print(f'2. {five_chars_names}')
print(f'3. {multiply_numbers}')