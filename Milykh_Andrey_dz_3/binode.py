"""
Класс узла (элемента) двухсвязного списка
"""


class BiNode:  # BiNode - Node for bidirectional linked list
    def __init__(self, data=None, next_node=None, previous_node=None):
        self.data = data
        self.next = next_node
        self.previous = previous_node

    # Get методы
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def get_previous(self):
        return self.previous

    # Set методы
    def set_data(self, data):
        self.data = data

    def set_next(self, next_node):
        self.next = next_node

    def set_previous(self, previous_node):
        self.previous = previous_node
