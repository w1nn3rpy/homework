from collections import Counter

"""
Напишите функцию, которая принимает строку и возвращает количество уникальных символов в строке.
Используйте для выполнения задачи lambda-функции и map и/или filter.
Сделайте так, чтобы алгоритм НЕ был регистрозависим: буквы разного регистра должны считаться одинаковыми.
"""

def count_unique_characters(string: str) -> int:
    unique_chars = Counter(string)
    count = sum(1 for count in unique_chars.values() if count == 1)
    return count


message = "Today is a beautiful day! The sun is shining and the birds are singing."
unique_count = count_unique_characters(message)
print("Количество уникальных символов в строке:", unique_count)