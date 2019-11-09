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

    def test_get_first(self):
        self.assertEqual(self.ll.get_first(), None)
        self.ll.insert_first('a')
        self.assertEqual(self.ll.get_first(), 'a')
        self.ll.insert_first('b')
        self.assertEqual(self.ll.get_first(), 'b')
        self.ll.insert_last('c')
        self.assertEqual(self.ll.get_first(), 'b')

    def test_get_last(self):
        self.assertEqual(self.ll.get_last(), None)
        self.ll.insert_first('a')
        self.assertEqual(self.ll.get_last(), 'a')
        self.ll.insert_first('b')
        self.assertEqual(self.ll.get_last(), 'a')
        self.ll.insert_last('c')
        self.assertEqual(self.ll.get_last(), 'c')

    def test_get_position(self):
        self.assertEqual(self.ll.get_position(1), None)
        self.ll.insert_first('a')
        self.assertEqual(self.ll.get_position(1), 'a')
        self.ll.insert_first('b')
        self.assertEqual(self.ll.get_position(1), 'b')
        self.assertEqual(self.ll.get_position(2), 'a')
        self.ll.insert_first('c')
        self.assertEqual(self.ll.get_position(1), 'c')
        self.assertEqual(self.ll.get_position(2), 'b')
        self.assertEqual(self.ll.get_position(3), 'a')
        self.ll.insert_last('d')
        self.assertEqual(self.ll.get_position(1), 'c')
        self.assertEqual(self.ll.get_position(2), 'b')
        self.assertEqual(self.ll.get_position(3), 'a')
        self.assertEqual(self.ll.get_position(4), 'd')
        self.assertEqual(self.ll.get_position(5), None)

    def test_get_position_with_invalid_position(self):
        with self.assertRaises(ValueError):
            self.ll.get_position(0)
        with self.assertRaises(ValueError):
            self.ll.get_position(-5)
        with self.assertRaises(ValueError):
            self.ll.get_position('string')
        with self.assertRaises(ValueError):
            self.ll.get_position(2.5)

    def test_remove_first(self):
        self.assertEqual(self.ll.remove_first(), None)
        self.ll.insert_first('a')
        self.assertEqual(self.ll.remove_first(), 'a')
        self.assertEqual(self.ll.remove_first(), None)
        self.ll.insert_first('a')
        self.ll.insert_first('b')
        self.ll.insert_first('c')
        self.ll.insert_first('d')
        self.assertEqual(self.ll.remove_first(), 'd')
        self.assertEqual(self.ll.remove_first(), 'c')
        self.assertEqual(self.ll.remove_first(), 'b')
        self.assertEqual(self.ll.remove_first(), 'a')
        self.assertEqual(self.ll.remove_first(), None)

    def test_remove_last(self):
        self.assertEqual(self.ll.remove_last(), None)
        self.ll.insert_first('a')
        self.assertEqual(self.ll.remove_last(), 'a')
        self.assertEqual(self.ll.remove_last(), None)
        self.ll.insert_first('a')
        self.ll.insert_first('b')
        self.ll.insert_first('c')
        self.ll.insert_first('d')
        self.assertEqual(self.ll.remove_last(), 'a')
        self.assertEqual(self.ll.remove_last(), 'b')
        self.assertEqual(self.ll.remove_last(), 'c')
        self.assertEqual(self.ll.remove_last(), 'd')
        self.assertEqual(self.ll.remove_last(), None)

    def test_remove(self):
        self.assertEqual(self.ll.remove('a'), None)
        self.ll.insert_first('a')
        self.assertEqual(self.ll.remove('a'), 'a')
        self.assertEqual(self.ll.remove('a'), None)
        self.ll.insert_first('a')
        self.ll.insert_first('b')
        self.ll.insert_first('c')
        self.ll.insert_first('d')
        self.assertEqual(self.ll.remove('f'), None)
        self.assertEqual(self.ll.remove('a'), 'a')
        self.assertEqual(self.ll.remove('c'), 'c')
        self.assertEqual(self.ll.remove('b'), 'b')
        self.assertEqual(self.ll.remove('d'), 'd')
        self.assertEqual(self.ll.remove('h'), None)
        self.ll.insert_first('a')
        self.ll.insert_first('b')
        self.ll.insert_first('c')
        self.ll.insert_first('d')
        self.assertEqual(self.ll.remove('d'), 'd')
        self.assertEqual(self.ll.remove('c'), 'c')

    def test_remove_position(self):
        self.assertEqual(self.ll.remove(3), None)
        self.ll.insert_first('a')
        self.assertEqual(self.ll.remove_position(1), 'a')
        self.assertEqual(self.ll.remove_position(1), None)
        self.ll.insert_first('a')
        self.ll.insert_first('b')
        self.ll.insert_first('c')
        self.ll.insert_first('d')
        self.assertEqual(self.ll.remove_position(1), 'd')
        self.assertEqual(self.ll.remove_position(1), 'c')
        self.assertEqual(self.ll.remove_position(1), 'b')
        self.assertEqual(self.ll.remove_position(1), 'a')
        self.assertEqual(self.ll.remove_position(1), None)
        self.ll.insert_first('a')
        self.ll.insert_first('b')
        self.ll.insert_first('c')
        self.ll.insert_first('d')
        self.assertEqual(self.ll.remove_position(4), 'a')
        self.assertEqual(self.ll.remove_position(2), 'c')
        self.assertEqual(self.ll.remove_position(2), 'b')
        self.assertEqual(self.ll.remove_position(2), None)
        self.assertEqual(self.ll.remove_position(1), 'd')

    def test_remove_position_with_invalid_position(self):
        with self.assertRaises(ValueError):
            self.ll.remove_position(0)
        with self.assertRaises(ValueError):
            self.ll.remove_position(-5)
        with self.assertRaises(ValueError):
            self.ll.remove_position('string')
        with self.assertRaises(ValueError):
            self.ll.remove_position(2.5)


if __name__ == '__main__':
    unittest.main()
