# create a node class for doubly linked list
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

# create class for doubly linked list


class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

        # method for printing
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next


doubly_linked_list = DoublyLinkedList(7)
doubly_linked_list.print_list()
