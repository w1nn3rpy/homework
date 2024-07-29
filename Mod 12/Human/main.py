class Human:
    __count = 0

    def __init__(self, name, age):
        if name.isalpha():
            self.__name = name
        else:
            raise SyntaxError('Имя должно состоять только из букв!')

        if str(age).isdigit() and 0 <= int(age) <= 100:
            self.__age = age
        else:
            raise ValueError('Возраст должен быть числом в диапазоне от 0 до 100')

        Human.__count += 1

    def __str__(self):
        return 'Это {}, ему {} лет.'.format(self.__name, self.__age)

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_count(self):
        return 'Количество людей: ' + str(self.__count)

    def set_age(self, age):
        self.__age = age

    def set_name(self, name):
        self.__name = name


vovan = Human('вован', 12)
grisha = Human('гриша', 52)
vasya = Human('vaasya', 12)

print(vovan)
print(grisha)

vovan.get_age()
vovan.get_name()
print(vovan.get_count())

vovan.set_name('Ludovik')
vovan.set_age(99)
print(vovan)

vovan._Human__age = 50
print(vovan)