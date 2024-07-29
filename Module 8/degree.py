def power(fl_num, nt_num):
    if nt_num == 1:
        return fl_num * nt_num
    return fl_num * power(fl_num, nt_num - 1)


float_num = float(input('Введите вещественное число: '))

int_num = int(input('Введите степень числа: '))

print(float_num, '**', int_num, '=', power(float_num, int_num))