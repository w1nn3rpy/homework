def is_palindrome_possible(word):
    # Считаем количество каждой буквы
    char_count = {}
    for char in word:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Подсчитываем количество символов, которые встречаются нечетное количество раз
    odd_count = sum(1 for count in char_count.values() if count % 2 != 0)

    # Для слова с четной длиной не должно быть символов, встречающихся нечетное количество раз
    # Для слова с нечетной длиной таких символов должно быть не больше одного
    return odd_count <= 1


def process_words(file_path):
    palindrome_count = 0

    with open(file_path, 'r') as file:
        words = file.readlines()

    with open('errors.log', 'w') as error_file:
        for word in words:
            word = word.strip()
            # Проверяем, содержит ли слово числа
            if any(char.isdigit() for char in word):
                error_file.write(f"ValueError: '{word}' contains a number.\n")
                raise ValueError('Ошибка записана в error.log')
            else:
                # Проверяем, можно ли составить палиндром
                if is_palindrome_possible(word):
                    palindrome_count += 1

    return palindrome_count


# Пример использования
file_path = 'words.txt'
palindrome_count = process_words(file_path)
print(f"Количество слов, из которых можно получить палиндром: {palindrome_count}")