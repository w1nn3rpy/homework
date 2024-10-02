from math import pi


class MyMath:

    @staticmethod
    def circle_len(radius):
        l = 2 * pi * radius
        return f'Длина окружности - {l} см'

    @staticmethod
    def circle_sq(radius):
        s = pi * radius ** 2
        return f'Площадь окружности - {s} см2'

    @staticmethod
    def cube_v(side):
        v = side ** 3
        return f'Объём куба - {v} см3'

    @staticmethod
    def sphere_sq(radius):
        sq = 4 * pi * radius
        return f'Площадь сферы - {sq} см2'


res_1 = MyMath.circle_len(radius=5)
res_2 = MyMath.circle_sq(radius=6)
print(res_1)
print(res_2)
