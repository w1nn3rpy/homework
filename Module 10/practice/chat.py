with open('chat_log.txt', 'w', encoding='utf-8') as chatfile:
    chatfile.write('Чат:\n')


def chat(chatfile):
    while True:
        try:
            name = input('Введите своё имя: ')
            action = int(input('''1 - Просмотреть текущий текст чата
2 - Написать сообщение
Введите цифру действия: '''))
            if action == 1:
                with open('chat_log.txt', 'r', encoding='utf-8') as chat_read:
                    print(chat_read.read())

            elif action == 2:
                with open('chat_log.txt', 'a', encoding='utf-8') as chat_write:
                    message = input('Введите сообщение: ')
                    if message:
                        chat_write.write(name + ': ' + str(message) + '\n')
                    else:
                        raise SyntaxError('Вы не ввели текст!')

            else:
                raise ValueError('Введите корректное значение')

        except (ValueError, SyntaxError) as val_er:
            print(str(val_er))


chat(chatfile)