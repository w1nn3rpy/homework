
class File:
    def __init__(self, name, method):
        print(f'Открыт контекстный менеджер {self.__class__.__name__}')
        self.name = name
        self.method = method

    def __enter__(self) -> 'File':
        self.file = open(self.name, self.method)
        return self

    def write(self, text: str) -> None:
        self.file.write(text)

    def __exit__(self, exc_type, exc_val, exc_tb) -> bool:
        self.file.close()
        return False


with File('example.txt', 'w') as file:
    file.write('Hello')

