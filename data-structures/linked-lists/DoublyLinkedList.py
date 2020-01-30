class Node:
    """
    The Node for the Doubly Linked List
    """

    def __init__(self, data):
        """
        The node constructor

        :param data: The node data
        """
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    Doubly Linked List
    """

    def __init__(self):
        """
        Doubly Linked List constructor
        """
        self.head = None
        self.size = 0

    def insert_first(self, data):
        pass

    def insert_last(self, data):
        pass

    def insert_after(self, data, position):
        pass

    def insert_before(self, data, position):
        pass

    def remove_first(self):
        pass

    def remove_last(self):
        pass

    def remove(self, data):
        pass

    def remove_position(self, position):
        pass

    def get_size(self):  # O(1)
        pass

    def traverse_list(self):  # O(n)
        pass

    def reverse_list(self):  # O(n)
        pass
