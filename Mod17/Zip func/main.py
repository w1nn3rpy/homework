from typing import List

letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]

"""
Даны список букв (letters) и список цифр (numbers). 
Каждый список состоит из N элементов. Создайте кортежи из пар элементов списков и запишите их в список results. 
Не используйте функцию zip. Решите задачу в одну строку (не считая print(results)).
"""

result: List[tuple] = list(map(lambda i: (letters[i], numbers[i]), range(min(len(letters), len(numbers)))))
print(result)

