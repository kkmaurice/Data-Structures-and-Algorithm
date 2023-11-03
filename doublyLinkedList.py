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

    # method for appending a new node to a doubly linked list
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    # method to pop item out of the doubly linked list
    def pop(self):

        if self.length == 0:
            return
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:

            self.tail = self.tail.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp.value

    # prepend a new node

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    # method for pop first
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp.value

    # get method for doubly linked list
    def get(self, index):
        if index < self.length or index > self.length:
            return None
        temp = self.head
        if index < self.length/2:
            for _ in range(index):
                temp = temp.next
        else:
            temp = self.tail
            for _ in range(self.length-1, index, -1):
                temp = temp.prev
        return temp

    # set method in doubly linked list

    def set_value(self, index, value):
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False

    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return None
        if index == 0:
            self.prepend(value)
        if index == self.length:
            self.append(value)

        before = self.get(index-1)
        after = before.next

        new_node.next = after
        new_node.prev = before
        before.next = new_node
        after.pre = new_node

        self.length += 1
        return True

    # Remove method

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop()

        temp = self.get(index)

        temp.next.prev = temp.prev
        temp.prev.next = temp.next
        temp.next = None
        temp.prev = None

        self.length -= 1
        return temp


doubly_linked_list = DoublyLinkedList(0)
doubly_linked_list.append(1)
doubly_linked_list.append(2)
doubly_linked_list.append(3)


doubly_linked_list.set_value(1, 4)
doubly_linked_list.print_list()
# doubly_linked_list.prepend(1)
# doubly_linked_list.print_list()
# print(doubly_linked_list.pop_first())
# print(doubly_linked_list.pop_first())
# print(doubly_linked_list.pop_first())
# doubly_linked_list.print_list()
# print(doubly_linked_list.get(1))
# print(doubly_linked_list.get(2))
# print(doubly_linked_list.pop())
# print(doubly_linked_list.pop())
