from queue import LifoQueue


class Stack:
    """
    Стек — это абстрактный тип данных, представляющий собой список элементов,
    организованных по принципу LIFO (англ. last in — first out, «последним пришёл — первым вышел»).
    """

    def __init__(self):
        self.main = LifoQueue()


class TaskManager:
    def __init__(self):
        self.stack = Stack()
        self.tasks = dict()

    def new_task(self, priority, task):
        if task not in self.tasks.keys():
            self.tasks[task] = [priority]
        else:
            self.tasks.get(task).append(priority)

    def set_stack(self, dictionary):
        for test in dictionary:
            self.stack.main.put(test)

    def get_stack(self):
        while not self.stack.main.empty():
            print(*self.stack.main.get())

    def get_tasks(self):
        return self.sort_tasks()

    def sort_tasks(self):
        sorted_dict = sorted(self.tasks.items(), reverse=True)
        return sorted_dict


manager = TaskManager()
manager.new_task('Сделать уборку', 2)
manager.new_task('Отдохнуть', 1)
# print(manager)
manager.new_task('Покурить', 1)
# print(manager)
manager.new_task('Поспать', 5)
# print(manager)
manager.set_stack(manager.get_tasks())
# print(manager)
manager.get_stack()
