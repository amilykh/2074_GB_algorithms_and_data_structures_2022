"""
Класс узла односвязного списка
"""


class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    # Get методы
    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    # Set методы
    def set_data(self, data):
        self.data = data

    def set_next(self, next_node):
        self.next = next_node
