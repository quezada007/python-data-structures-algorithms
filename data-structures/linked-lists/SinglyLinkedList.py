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
        """
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def insert_last(self, data):  # O(n)
        """
        Insert a node a the end of the list and increment the list size

        :param data: The node data
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
            # Insert at the end of the list
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
        # If the list is empty, return None
        if self.head is None:
            return None
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            return current.data

    def get_position(self, position):  # O(n)
        """
        Get the node at the given position of the list

        :param position: The position (index) of the list to retrieve the data
        :return: The data of the node at a given position
        """
        # Check for invalid position values
        if not isinstance(position, int) or position < 1:
            raise ValueError('The position needs to be an integer greater than 0')
        # If the list is empty, return None
        if self.head is None:
            return None
        elif position == 1:
            return self.head.data
        else:
            index = 1
            current = self.head
            while index <= position and current is not None:
                if index == position:
                    return current.data
                index += 1
                current = current.next
            return None

    def remove_first(self):  # O(1)
        """
        Delete the first node of the list

        :return: The data of the deleted node
        """
        current = self.head
        # If head is not None, then remove it
        if current is not None:
            self.head = self.head.next
            current.next = None
            self.size -= 1
            return current.data
        # If list is empty, return None
        else:
            return None

    def remove_last(self):  # O(n)
        """
        Delete the last node of the list

        :return: The data of the deleted node
        """
        # If the list is empty, then return None
        if self.head is None:
            return None
        # If there is only 1 Node in the list, then delete the head
        elif self.head.next is None:
            current = self.head
            self.head = None
            self.size -= 1
            return current.data
        # If the list has more than 1 Node, go to the end of the list
        else:
            current = self.head
            while current.next.next is not None:
                current = current.next
            deleted_node = current.next
            current.next = None
            self.size -= 1
            return deleted_node.data

    def remove(self, data):  # O(n)
        """
        Delete the node that contains the given data

        :param data: The data to search in the nodes
        :return: The data of the deleted node
        """
        # If the list is empty, then return None
        if self.head is None:
            return None
        # The list is not empty
        else:
            current = self.head
            previous = None
            while current.data != data and current.next is not None:
                previous = current
                current = current.next
            if current.data == data:
                # Check to make sure that the data is not in the head
                if previous is not None:
                    previous.next = current.next
                    current.next = None
                # If the data is in the head, then delete the head
                else:
                    self.head = current.next
                self.size -= 1
                return current.data

    def remove_position(self, position):  # O(n)
        """
        Delete a node at a given position

        :param position: The position (index) of the node that is going to get deleted
        :return: The data of the deleted node
        """
        # Check for invalid position values
        if not isinstance(position, int) or position < 1:
            raise ValueError('The position needs to be an integer greater than 0')
        # If the list is empty, return None
        if self.head is None:
            return None
        # The list is not empty
        else:
            index = 1
            current = self.head
            previous = None
            while index < position and current.next is not None:
                previous = current
                current = current.next
                index += 1
            if index == position:
                # Check to make sure that the data is not in the head
                if previous is not None:
                    previous.next = current.next
                    current.next = None
                # If the data is in the head, then delete the head
                else:
                    self.head = current.next
                self.size -= 1
                return current.data

    def get_size(self):  # O(1)
        """
        The size (length) of the list

        :return: The length of the list
        """
        return self.size

    def traverse_list(self):  # O(n)
        """
        Traverse the entire list

        :return: The list in a comma delimited format
        """
        node_list = ''
        current = self.head
        while current is not None:
            node_list += str(current.data) + ', '
            current = current.next
        return node_list.strip(', ')

    def reverse_list(self):  # O(n)
        """
        Reverse the Singly Linked List
        """
        previous = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous
