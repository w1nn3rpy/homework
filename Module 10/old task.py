import io


def iter_num(nums):
    summ = 0
    for line in nums:
        for char in line:
            if char.isdigit():
                summ += int(char)
    return summ


try:
    nums = open('numbers1.txt', 'r')
    answer = open('answer1.txt', 'w')
except FileExistsError:
    print('Невозможно создать файл. Файл с таким названием уже существует.')
except FileNotFoundError:
    print('Невозможно открыть файл. Файла с таким названием не существует.')
else:
    try:
        answer.write(str(iter_num(nums)))
    except io.UnsupportedOperation:
        print('Файл пустой')
    else:
        nums.close()
        answer.close()
        print('Закрываем файлы...')
finally:
    if nums.closed and answer.closed:
        print('Файлы закрыты.')

