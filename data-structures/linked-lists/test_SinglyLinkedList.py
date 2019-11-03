import unittest
from SinglyLinkedList import SinglyLinkedList


class TestSinglyLinkedList(unittest.TestCase):

    def setUp(self):
        self.ll = SinglyLinkedList()

    def test_insert_first(self):
        self.assertEqual(self.ll.head, None)
        self.ll.insert_first('a')
        self.assertEqual(self.ll.head.data, 'a')
        self.ll.insert_first('b')
        self.assertEqual(self.ll.head.data, 'b')
        self.assertEqual(self.ll.head.next.data, 'a')
        self.ll.insert_first('c')
        self.assertEqual(self.ll.head.data, 'c')
        self.assertEqual(self.ll.head.next.data, 'b')
        self.assertEqual(self.ll.head.next.next.data, 'a')

    def test_insert_last(self):
        self.assertEqual(self.ll.head, None)
        self.ll.insert_last('a')
        self.assertEqual(self.ll.head.data, 'a')
        self.ll.insert_last('b')
        self.assertEqual(self.ll.head.data,'a')
        self.assertEqual(self.ll.head.next.data, 'b')
        self.ll.insert_last('c')
        self.assertEqual(self.ll.head.data, 'a')
        self.assertEqual(self.ll.head.next.data, 'b')
        self.assertEqual(self.ll.head.next.next.data, 'c')

    def test_insert(self):
        self.assertEqual(self.ll.head, None)
        self.ll.insert('a', 1)
        self.assertEqual(self.ll.head.data, 'a')
        self.ll.insert('b', 2)
        self.assertEqual(self.ll.head.next.data, 'b')
        self.ll.insert('c', 2)
        self.assertEqual(self.ll.head.data, 'a')
        self.assertEqual(self.ll.head.next.data, 'c')
        self.assertEqual(self.ll.head.next.next.data, 'b')
        self.ll.insert('d', 4)
        self.assertEqual(self.ll.head.data, 'a')
        self.assertEqual(self.ll.head.next.data, 'c')
        self.assertEqual(self.ll.head.next.next.data, 'b')
        self.assertEqual(self.ll.head.next.next.next.data, 'd')
        self.ll.insert('e', 4)
        self.assertEqual(self.ll.head.data, 'a')
        self.assertEqual(self.ll.head.next.data, 'c')
        self.assertEqual(self.ll.head.next.next.data, 'b')
        self.assertEqual(self.ll.head.next.next.next.data, 'e')
        self.assertEqual(self.ll.head.next.next.next.next.data, 'd')
        self.ll.insert('f', 6)
        self.assertEqual(self.ll.head.data, 'a')
        self.assertEqual(self.ll.head.next.data, 'c')
        self.assertEqual(self.ll.head.next.next.data, 'b')
        self.assertEqual(self.ll.head.next.next.next.data, 'e')
        self.assertEqual(self.ll.head.next.next.next.next.data, 'd')
        self.assertEqual(self.ll.head.next.next.next.next.next.data, 'f')
        self.ll.insert('g', 2)
        self.assertEqual(self.ll.head.data, 'a')
        self.assertEqual(self.ll.head.next.data, 'g')
        self.assertEqual(self.ll.head.next.next.data, 'c')
        self.assertEqual(self.ll.head.next.next.next.data, 'b')
        self.assertEqual(self.ll.head.next.next.next.next.data, 'e')
        self.assertEqual(self.ll.head.next.next.next.next.next.data, 'd')
        self.assertEqual(self.ll.head.next.next.next.next.next.next.data, 'f')

    def test_insert_with_invalid_position(self):
        with self.assertRaises(ValueError):
            self.ll.insert('a', 0)
        with self.assertRaises(ValueError):
            self.ll.insert('a', -5)
        with self.assertRaises(ValueError):
            self.ll.insert('a', 'string')
        with self.assertRaises(ValueError):
            self.ll.insert('a', 2.5)


if __name__ == '__main__':
    unittest.main()
