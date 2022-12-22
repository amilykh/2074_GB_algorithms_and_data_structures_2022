from node import Node


class LinkedList:
    """Класс односвязного списка"""
    def __init__(self):
        self.head = None

    def find(self, data):
        cur_node = self.head
        while cur_node is not None:
            if cur_node == data:
                return cur_node
            else:
                cur_node = cur_node.get_next()
        return None

    # добавление элемента в конец односвязного списка
    def append(self, data):
        new_node = Node(data)
        cur_node = self.head
        if cur_node is None:
            self.head = new_node  # если односвязный список пуст
            return
        while cur_node.get_next():
            cur_node = cur_node.get_next()
        cur_node.set_next(new_node)

    def show(self):
        cur_node = self.head
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

    def push_front(self, data):
        new_node = Node(data)
        first_node = self.head
        new_node.set_next(first_node)
        self.head = new_node

    def remove_back(self):
        cur_node = self.head
        while cur_node.get_next().get_next() is not None:
            cur_node = cur_node.get_next()
        cur_node.set_next(None)  # ! - удалили последний элемент

    def remove_front(self):
        cur_node = self.head
        self.head = cur_node.get_next()  # ! - удалили первый элемент

    def value_at(self, index):
        cur_node = self.head
        count = 0
        while cur_node is not None:
            if count == index:
                return cur_node.get_data()
            count += 1
            cur_node = cur_node.get_next()

        print("Index is out of range")

    def insert(self, index, data):
        new_node = Node(data)
        cur_node = self.head
        count = 0
        while cur_node.get_next() is not None:
            if index == 0:  # хотим вставить элемент в начало
                self.push_front(data)
                return
            elif count + 1 == index:
                the_node_after_cur = cur_node.get_next()
                cur_node.set_next(new_node)
                new_node.set_next(the_node_after_cur)
                return
            count += 1
            cur_node = cur_node.get_next()
        print("Index is out of range")

    def remove(self, index):
        cur_node = self.head
        count = 0
        while cur_node.get_next() is not None:
            if index == 0:
                self.remove_front()
                return
            elif count + 1 == index:
                the_node_to_remove = cur_node.get_next()
                the_node_after_removed = the_node_to_remove.get_next()
                cur_node.set_next(the_node_after_removed)
                return
            count += 1
            cur_node = cur_node.get_next()
        print("Index is out of range")

    # метод разворота односвязного списка
    def reverse(self):
        cur_node = self.head
        if cur_node is None:
            print("The list has no element")
            return
        prev_node = None
        # next_node = None
        while cur_node is not None:
            next_node = cur_node.get_next()
            cur_node.set_next(prev_node)
            prev_node = cur_node
            cur_node = next_node
        self.head = prev_node
