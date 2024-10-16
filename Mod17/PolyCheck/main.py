from collections import Counter

"""
Используя модуль collections, реализуйте функцию can_be_poly, 
`которая принимает на вход строку и проверяет, можно ли получить из неё палиндром. 
"""

def can_be_poly(string: str) -> bool:
    char_counter = Counter(string)
    odd_count = sum(1 for count in char_counter.values() if count % 2 != 0)
    return odd_count <= 1

print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))