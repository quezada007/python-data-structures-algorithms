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
