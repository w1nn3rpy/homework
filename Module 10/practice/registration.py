def valid(line):
    if len(line) < 3:
        raise IndexError("Пустая строка")
    name, email, age = line
    if not name.isalpha():
        raise NameError("Поле 'Имя' содержит не только буквы")
    if '@' not in email or '.' not in email:
        raise SyntaxError("Поле 'Имейл' не содержит @ и точку")
    if not age.isdigit() or not 10 <= int(age) <= 99:
        raise ValueError("Поле 'Возраст' не представляет число от 10 до 99")
    return True


with open('registration.txt', 'r', encoding='utf-8') as users_data:
    with open('registration_good.log', 'w', encoding='utf-8') as good:
        with open('registration_bad.log', 'w', encoding='utf-8') as error:
            for lines in users_data.readlines():
                lines = lines.rstrip()
                line = lines.split()
                try:
                    if valid(line) is True:
                        good.write(lines + '\n')
                    else:
                        continue

                except IndexError:
                    error.write('Пустая строка\n')
                except NameError:
                    error.write(lines + ' Поле "Имя" содержит не только буквы\n')
                except SyntaxError:
                    error.write(lines + ' Поле «Имейл» НЕ содержит @ и точку\n')
                except ValueError:
                    error.write(lines + ' Поле «Возраст» НЕ представляет число от 10 до 99\n')
