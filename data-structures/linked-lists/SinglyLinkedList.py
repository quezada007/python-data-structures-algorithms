class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert_first(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
        self.size += 1

    def insert_last(self, data):
        if self.head is None:
            self.head = Node(data)
            self.size += 1
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = Node(data)
            self.size += 1

    def insert(self, data, position):
        # Check for invalid position values
        if position < 1 or type(position) != int:
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

    def get_first(self):
        pass

    def get_last(self):
        pass

    def get_position(self, position):
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
