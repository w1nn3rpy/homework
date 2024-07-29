class MyDict(dict):
    """
    Класс словаря для переопределения метода get
    """
    def get(self, value, return_value=0):
        if value in self.keys():
            return self[value]
        else:
            return return_value


"""Переопределенный словарь"""

mydict = MyDict({'a': 2, 'b': 3, 'c': 5})
print(mydict)
for i_dict in mydict.items():
    print(i_dict)
print(mydict.get('a'))
print(mydict.get('c'))
print(mydict.get('test'))  # Возвращает 0


"""Обычный словарь"""

original_dict = dict({'a': 2, 'b': 3, 'c': 5})
print(original_dict)
for i_dict in original_dict.items():
    print(i_dict)
print(original_dict.get('a'))
print(original_dict.get('c'))
print(original_dict.get('test'))  # Возвращает None
