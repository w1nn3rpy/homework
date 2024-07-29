def ask_user(quest,
             message='Неверный ввод. Введите да или нет',
             retries=3):
    while True:
        answer = input(quest).lower()
        if answer == 'да':
            return 1
        if answer == 'нет':
            return 0
        retries -= 1
        if retries == 0:
            print('Количество попыток истекло')
            break
        print(message)
        print('Осталось попыток:', retries)


print(ask_user('Вы действительно хотите выйти? ', message='Хуевый ответ, да или нет?)', retries=1))
