
BRUCE_WILLIS = 42

input_data = input('Введите строку: ')
try:
    leeloo = int(input_data[4])
    result = BRUCE_WILLIS * leeloo
    print(f'- Leeloo Dallas! Multi-pass № {result}!')

except ValueError:
    print('Невозможно преобразовать к числу')
except IndexError:
    print('Выход за границы списка')
except:
    print('Остальные исключения')