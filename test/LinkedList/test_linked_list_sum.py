import unittest
from src.LinkedList.linked_list_sum import sum_equal_lists
from src.LinkedList.linked_list_realization import Node, LinkedList
class TestSumList(unittest.TestCase):
    def test_common_list_sum(self):
        n1=Node(12)
        n2=Node(144)
        n3=Node(55)        
        test_list=LinkedList()
        test_list.add_in_tail(n1)
        test_list.add_in_tail(n2)
        test_list.add_in_tail(n3)
        n3=Node(-12)
        n4=Node(-144)
        n5=Node(-56)        
        test_list_2=LinkedList()
        test_list_2.add_in_tail(n3)
        test_list_2.add_in_tail(n4)
        test_list_2.add_in_tail(n5)
        sum_list=sum_equal_lists(test_list, test_list_2)
        self.assertEqual(sum_list.head.value, 0, "Sum_list have zero in the beginning")
        self.assertEqual(sum_list.tail.value, -1, "Sum_list have zero in the end")
        self.assertEqual(sum_list.len(),3, "Length is 3")

    def test_empty_list_sum(self):
        n1=Node(12)
        n2=Node(144)
        n3=Node(55)        
        test_list=LinkedList()
        test_list.add_in_tail(n1)
        test_list.add_in_tail(n2)
        test_list.add_in_tail(n3)
        n3=Node(-12)
        n4=Node(-144)
        n5=Node(-56)        
        test_list_2=LinkedList()
        with self.assertRaises(Exception):

            sum_list=sum_equal_lists(test_list, test_list_2)
        # self.assertIsNone(sum_list.head, "List head is None")
        # self.assertIsNone(sum_list.tail, "List head is None")
        # self.assertEqual(sum_list.len(),0, "Length is 0")