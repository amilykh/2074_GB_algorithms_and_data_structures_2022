from binode import BiNode


class BiLinkedList:  # Bi - bidirectional
    """Класс двухсвязного списка"""
    def __init__(self):
        self.head = None

    # добавление элемента в пустой двухсвязный список
    def insert_in_emptylist(self, data):
        if self.head is None:
            new_node = BiNode(data)
            self.head = new_node
        else:
            print("list is not empty")

    # добавление элемента в начало двухсвязного списка
    def push_front(self, data):
        new_node = BiNode(data)
        if self.head is None:
            self.head = new_node
            print("node inserted")
            return
        new_node.next = self.head
        self.head.previous = new_node
        self.head = new_node

    # добавление элемента в конец двусвязанного списка
    def append(self, data):
        new_node = BiNode(data)
        cur_node = self.head
        if cur_node is None:  # если связный список пуст
            self.head = new_node
            return
        while cur_node.get_next():
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)
        new_node.previous = cur_node

    def show(self):
        cur_node = self.head
        if cur_node is None:
            print("List has no element")
            return
        output = ""
        while cur_node is not None:
            output += str(cur_node.get_data()) + " -> "
            cur_node = cur_node.get_next()
        print(output)

    def length(self):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            count += 1
            cur_node = cur_node.get_next()
        print(count)

    def remove_front(self):
        cur_node = self.head
        if cur_node is None:
            print("The list has no element to delete")
            return
        self.head = cur_node.get_next()  # ! - удалили первый элемент
        self.head.previous = None

    def remove_back(self):
        cur_node = self.head
        if cur_node is None:
            print("The list has no element to delete")
            return
        while cur_node.get_next().get_next() is not None:
            cur_node = cur_node.get_next()
        cur_node.set_next(None)  # ! - удалили последний элемент

    # метод разворота двусвязного списка
    def reverse(self):
        cur_node = self.head
        if cur_node is None:
            print("The list has no element")
        cur_node = self.head
        next_node = cur_node.next
        cur_node.next = None
        cur_node.previous = next_node
        while next_node is not None:
            next_node.previous = next_node.next
            next_node.next = cur_node
            cur_node = next_node
            next_node = next_node.previous
        self.head = cur_node
