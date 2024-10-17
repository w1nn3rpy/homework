import re

text = 'Amit 34-3456 12-05-2007, XYZ 56-4532 11-11-2011, ABC 67-8945 12-01-2009'

"""
Используя регулярные выражения, напишите программу, получающую список всех дат, которые встречаются в строке. 
"""

date_pattern = r'\d{2}-\d{2}-\d{4}'
dates = re.findall(date_pattern, text)
print(dates)