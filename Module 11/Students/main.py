class Student:

    def __init__(self):
        self.name = input('Введите имя и фамилию: ')
        self.group = int(input('Введите номер группы: '))
        self.performance = input('Введите 5 последних оценок через пробел: ').split()

    def mid_grade(self):
        num = 0
        for grade in self.performance:
            num += int(grade)
        num /= len(self.performance)
        return num

    def print_info(self):
        print('Имя: {}'.format(self.name))
        print('Группа: {}'.format(self.group))
        print('Оценки: {}'.format(self.performance))


alex = Student()
borya = Student()
dima = Student()

students = [alex, borya, dima]

while students:
    temp = students[0]
    for student in students:
        if student.mid_grade() >= temp.mid_grade():
            temp = student
            temp.print_info()
            students.remove(student)
