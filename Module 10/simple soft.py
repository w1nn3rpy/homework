text = input('Введите текст для записи в файл: ')

try:
    with open('new result.txt', 'w') as result:
        result.write(text)
except FileExistsError:
    print('Ошибка! Файл с таким названием уже существует!')
except ValueError:
    print('Нельзя преобразовать данные в целое')
except:
    print('Непредвиденная ошибка')
else:
    result.close()
    print('Файл закрыт')
finally:
    if result.closed is True:
        print('Проверка прошла успешно. Файл закрыт.')
