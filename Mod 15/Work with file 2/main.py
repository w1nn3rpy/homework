class File:
    def __init__(self, name, **method):
        print(f'============Открыт контекстный менеджер {self.__class__.__name__}============')
        self.name = name
        self.method = method

    def __enter__(self) -> 'File':
        try:
            self.file = open(self.name, **self.method)
            return self
        except FileNotFoundError:
            print(f'Файл {self.name} не найден.\nСоздаю файл {self.name}\nОткрываю файл {self.name} в режиме записи')
            self.file = open(self.name, 'w')
            self.file.write(input(f'Введите текст для записи в новый файл "{self.name}": '))
            return self.__enter__()

    def read(self):
        text = self.file.read()
        print('============Text from the file============')
        return text

    def write(self, text: str) -> None:
        self.file.write(text)

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        try:
            if self.file:
                self.file.close()
        except (FileNotFoundError, FileExistsError, OSError):
            return True
        return False


with File('example.txt') as file:
    print(file.read())