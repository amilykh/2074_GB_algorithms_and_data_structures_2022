# Однонаправленный связный список


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def append(self, val):
        end = Node(val)  # создание нового узла end
        n = self  # ссылка на текущий узел
        while n.next:
            n = n.next
        n.next = end


# ll - сокращение от Linked List
ll = Node(1)
ll.append(2)
ll.append(3)

node = ll
# для начала выведем первый узел, а затем запустим цикл while
# для вывода всех последующих узлов
print(node.data)
while node.next:
    node = node.next
    print(node.data)
