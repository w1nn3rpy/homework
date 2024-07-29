with open('people.txt', 'r', encoding='utf-8') as names:
    chars_count = 0

    for num_of_line, line in enumerate(names, start=1):
        try:
            clean_line = line.strip()
            chars_count += len(clean_line)
            if len(clean_line) < 3:
                raise ValueError
        except ValueError:
            print('В строке', num_of_line, 'меньше трех символов.')

print('Сумма всех символов:', chars_count)
