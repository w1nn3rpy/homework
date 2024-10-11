class Person:
    def __init__(self, name: str, age: int, other: str):
        self._name = name
        self._age = age
        self._other = other


    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def other(self):
        return self._other

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @age.setter
    def age(self, new_age: int):
        self._age = new_age

    @other.setter
    def other(self, other):
        self._other = other


aii = Person('Aii', 12, 'just ai')
uaa = Person('Uaa', 24, 'hi')
china = Person('China', 100, 'nihao')
russia = Person('Russia', 55, 'zdarova')


persons = [aii, uaa, china, russia]

for i in persons:
    print(i.name, i.age, i.other)

sorted_persons = sorted(persons, key=lambda x: x.age)

print('\n')

for i in sorted_persons:
    print(i.name, i.age, i.other)