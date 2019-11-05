class Node:
    """
    The Node for the Singly Linked List
    """

    def __init__(self, data):
        """
        The Node constructor

        :param data: The node data
        """
        self.data = data
        self.next = None


class SinglyLinkedList:
    """
    Singly Linked List
    """

    def __init__(self):
        """
        The Singly Linked List constructor
        """
        self.head = None
        self.size = 0

    def insert_first(self, data):  # O(1)
        """
        Insert a node at the beginning of the list and increment the list size

        :param data: The node data
        :return:
        """
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def insert_last(self, data):  # O(n)
        """
        Insert a node a the end of the list and increment the list size

        :param data: The node data
        :return:
        """
        # Check to see if the list is empty
        if self.head is None:
            self.head = Node(data)
            self.size += 1
        # If the list is not empty then insert a node at the end
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)
            self.size += 1

    def insert(self, data, position):  # O(n)
        """
        Insert a node at a specific position in the list and increment the list size

        :param data: The node data
        :param position: The position (index) of the list to insert the new node
        :return:
        """
        # Check for invalid position values
        if not isinstance(position, int) or position < 1:
            raise ValueError('The position needs to be an integer greater than 0')
        # If position is 1 then insert at the head
        if position == 1:
            self.insert_first(data)
        else:
            index = 1
            current = self.head
            node = Node(data)
            # Insert in the middle of the list
            while index <= position and current.next is not None:
                if index == position - 1:
                    node.next = current.next
                    current.next = node
                    self.size += 1
                index += 1
                current = current.next
            # Insert at the tail of the list
            if index + 1 == position:
                current.next = node
                self.size += 1

    def get_first(self):  # O(1)
        """
        Get the first node of the list

        :return: The data of the first node
        """
        return self.head.data if self.head is not None else None

    def get_last(self):  # O(n)
        """
        Get the last node of the list

        :return: The data of the last node
        """
        if self.head is None:
            return None
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            return current.data

    def get_position(self, position):  # O(n)
        pass

    def remove_first(self):
        pass

    def remove_last(self):
        pass

    def remove(self, data):
        pass

    def remove_position(self, position):
        pass

    def size(self):
        return self.size

    def traverse_list(self):
        node_list = ''
        current = self.head
        while current is not None:
            node_list += current.data + ', '
            current = current.next
        print(node_list.strip(', '))
