from collections import Counter

"""
Используя модуль collections, реализуйте функцию can_be_poly, 
`которая принимает на вход строку и проверяет, можно ли получить из неё палиндром. 
"""

def can_be_poly(string: str) -> bool:
    return len(list(filter(lambda x: x % 2, Counter(string).values()))) <= 1

print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))