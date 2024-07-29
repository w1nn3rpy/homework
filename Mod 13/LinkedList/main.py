class Node:
    def __init__(self, data: any = None) -> None:
        self.data = data
        self.next = None
        

class LinkedList:
    def __init__(self) -> None:
        self.head = None

    def append(self, data: any) -> None:
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def get(self, index: int) -> any:
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.data
            count += 1
            current = current.next
        raise IndexError('List index out of range')

    def remove(self, index: int) -> None:
        if self.head is None:
            raise IndexError('List index out of range')

        temp = self.head

        if index == 0:
            self.head = temp.next
            temp = None
            return

        for i in range(index - 1):
            temp = temp.next
            if temp is None:
                raise IndexError('List index out of range')

        if temp is None or temp.next is None:
            raise IndexError('List index out of range')

        next = temp.next.next
        temp.next = None
        temp.next = next


llist = LinkedList()
llist.append((3, 2, 1))
llist.append(20)
print(llist.get(0))
print(llist.get(1))
llist.remove(0)
print(llist.get(0))
print(llist.get(1))