import unittest
from src.OrderedList.ordered_list_int import OrderedList, Node, OrderedStringList

class TestOrderedList(unittest.TestCase):
    def setUp(self):
        self.test_value=[123,1000,-432,12345,0,-321]
        self.test_string_value=["Alabama ", "Amalgama", "Gavana", "sdfiwe", "    "]
        
    def test_add_empty_one_asc(self):
        o_list_asc=OrderedList(asc=True)
        test_value=self.test_value
        self.assertEqual(o_list_asc.len(), 0, "The size is 0")
        o_list_asc.add(test_value[0])
        self.assertEqual(o_list_asc.len(), 1, "The size is 1")
        self.assertEqual(o_list_asc.head.value, test_value[0], f"The head is {test_value[0]}" )
        self.assertEqual(o_list_asc.tail.value, test_value[0], f"The head is {test_value[1]}" )

    def test_add_empty_one_desc(self):
        o_list_asc=OrderedList(asc=False)
        test_value=self.test_value
        self.assertEqual(o_list_asc.len(), 0, "The size is 0")
        o_list_asc.add(test_value[0])
        self.assertEqual(o_list_asc.len(), 1, "The size is 1")
        self.assertEqual(o_list_asc.head.value, test_value[0], f"The head is {test_value[0]}" )
        self.assertEqual(o_list_asc.tail.value, test_value[0], f"The tail is {test_value[0]}" )

    def test_add_two_asc_1(self):
        o_list_asc=OrderedList(asc=True)
        test_value=self.test_value
        self.assertEqual(o_list_asc.len(), 0, "The size is 0")
        o_list_asc.add(test_value[0])
        o_list_asc.add(test_value[1])
        self.assertEqual(o_list_asc.len(), 2, "The size is 2")
        self.assertEqual(o_list_asc.head.value, test_value[0], f"The head is {test_value[0]}" )
        self.assertEqual(o_list_asc.tail.value, test_value[1], f"The head is {test_value[1]}" )

    def test_add_two_asc_2(self):
        o_list_asc=OrderedList(asc=True)
        test_value=self.test_value
        self.assertEqual(o_list_asc.len(), 0, "The size is 0")
        o_list_asc.add(test_value[0])
        o_list_asc.add(test_value[2])
        self.assertEqual(o_list_asc.len(), 2, "The size is 2")
        self.assertEqual(o_list_asc.head.value, test_value[2], f"The head is {test_value[2]}" )
        self.assertEqual(o_list_asc.tail.value, test_value[0], f"The head is {test_value[0]}" )

    def test_add_empty_one_desc_2(self):
        o_list_asc=OrderedList(asc=False)
        test_value=self.test_value
        self.assertEqual(o_list_asc.len(), 0, "The size is 0")
        o_list_asc.add(test_value[0])
        self.assertEqual(o_list_asc.len(), 1, "The size is 1")
        self.assertEqual(o_list_asc.head.value, test_value[0], f"The head is {test_value[0]}" )
        self.assertEqual(o_list_asc.tail.value, test_value[0], f"The tail is {test_value[0]}" )

    def test_delete_empty_list(self):
        o_list_asc=OrderedList(asc=True)
        self.assertIsNone(o_list_asc.delete(10), "Should be non if the list is empty")
    
    def test_delete_empty_list_string(self):
        o_list_asc=OrderedStringList(asc=True)
        self.assertIsNone(o_list_asc.delete('Hello'), "Should be non if the list is empty")

    def test_add_three_asc(self):
        o_list_asc=OrderedList(asc=True)
        test_value=self.test_value
        self.assertEqual(o_list_asc.len(), 0, "The size is 0")
        o_list_asc.add(test_value[0])
        o_list_asc.add(test_value[1])
        o_list_asc.add(test_value[2])
        
        self.assertEqual(o_list_asc.len(), 3, "The size is 3")
        self.assertEqual(o_list_asc.head.value, test_value[2], f"The head is {test_value[2]}" )
        self.assertEqual(o_list_asc.tail.value, test_value[1], f"The head is {test_value[1]}" )

    def test_add_three_desc(self):
        o_list_asc=OrderedList(asc=False)
        test_value=self.test_value
        self.assertEqual(o_list_asc.len(), 0, "The size is 0")
        o_list_asc.add(test_value[0])
        o_list_asc.add(test_value[1])
        o_list_asc.add(test_value[2])
        self.assertEqual(o_list_asc.len(), 3, "The size is 3")
        self.assertEqual(o_list_asc.head.value, test_value[1], f"The head is {test_value[1]}" )
        self.assertEqual(o_list_asc.tail.value, test_value[2], f"The head is {test_value[2]}" )

    def test_add_ten_desc(self):
        o_list_asc=OrderedList(asc=False)
        test_value=self.test_value
        self.assertEqual(o_list_asc.len(), 0, "The size is 0")
        for item in test_value:
            o_list_asc.add(item)
        self.assertEqual(o_list_asc.len(), len(test_value), f"The size is {len(test_value)}")
        self.assertEqual(o_list_asc.head.value, test_value[3], f"The head is {test_value[3]}" )
        self.assertEqual(o_list_asc.tail.value, test_value[2], f"The tail is {test_value[2]}" )
        for i in range(10):
            o_list_asc.add(i)
        self.assertEqual(o_list_asc.len(), 16, "The size is 15")
        self.assertEqual(o_list_asc.head.value, test_value[3], f"The head is {test_value[4]}" )
        self.assertEqual(o_list_asc.tail.value, test_value[2], f"The head is {test_value[2]}" )
    
    def test_delete_one(self):
        o_list_asc=OrderedList(asc=True)
        self.assertEqual(o_list_asc.len(), 0, "The size is 0")
        o_list_asc.add(9)        
        self.assertEqual(o_list_asc.len(), 1, "The size is 1")
        o_list_asc.delete(9)
        self.assertEqual(o_list_asc.len(), 0, "The size is 0")
    
    def test_delete_from_head(self):
        test_value=self.test_value
        o_list_asc=OrderedList(asc=True)
        o_list_asc.add(test_value[0])
        o_list_asc.add(test_value[1])
        o_list_asc.add(test_value[2])
        self.assertEqual(o_list_asc.len(), 3, "The size is 3")
        self.assertEqual(o_list_asc.head.value, test_value[2], f"Head is {test_value[2]}")
        self.assertEqual(o_list_asc.tail.value, test_value[1], f"Tail is {test_value[1]}")
        o_list_asc.delete(test_value[2])
        self.assertEqual(o_list_asc.len(), 2, "The size is 2")        
        self.assertEqual(o_list_asc.head.value, test_value[0], f"Head is {test_value[0]}")
        self.assertEqual(o_list_asc.tail.value, test_value[1], f"Tail is {test_value[1]}")

    def test_delete_from_tail(self):
        test_value=self.test_value
        o_list_asc=OrderedList(asc=True)
        for item in test_value:
            o_list_asc.add(item)
        self.assertEqual(o_list_asc.len(), len(test_value), f"The size is {len(test_value)}")
        self.assertEqual(o_list_asc.head.value, test_value[2], f"Head is {test_value[2]}")
        self.assertEqual(o_list_asc.tail.value, test_value[3], f"Tail is {test_value[3]}")
        o_list_asc.delete(test_value[3])
        self.assertEqual(o_list_asc.len(), len(test_value)-1, f"The size is {len(test_value)-1}")        
        self.assertEqual(o_list_asc.head.value, test_value[2], f"Head is {test_value[0]}")
        self.assertEqual(o_list_asc.tail.value, test_value[1], f"Tail is {test_value[1]}")
    
    def test_find_desc(self):
        test_value=self.test_value
        o_list_desc=OrderedList(asc=False)
        for item in test_value:
            o_list_desc.add(item)
        #r=o_list_desc.get_all()
        

    
    def test_string_list(self):
        test_string=self.test_string_value
        strin_o_list_desc=OrderedStringList(asc=False)
        for string in test_string:
            strin_o_list_desc.add(string)
        print(strin_o_list_desc.head.value)
        print(strin_o_list_desc.tail.value)
        strin_o_list_desc.delete("")
        print(strin_o_list_desc.tail.value)
        strin_o_list_desc.delete("Amalgama")
        print(strin_o_list_desc.head.value)
        strin_o_list_desc.delete("Alabama")

        




