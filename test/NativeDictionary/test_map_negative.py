#Test1:
#Get from empty list

#Test2:
#Insert to full array

import unittest
from src.NativeDictionary.map import NativeDictionary

class TestNativeDictionaryNegative(unittest.TestCase):
    def setUp(self):
        test_map = NativeDictionary(5)
        TEST_STRINGS_KEYS = ["name", "birthday", "profession", "institute", "hobby"]
        TEST_STRINGS_VALUES = ["Irina", "16.09.1991", "Programmer", "MSU", "cats"]
        for pos in range(len(TEST_STRINGS_KEYS)):
            print(f"hash_fun of {TEST_STRINGS_KEYS[pos]} is {test_map.hash_fun(TEST_STRINGS_KEYS[pos])}")
            print(f"{pos} string of keys {TEST_STRINGS_KEYS[pos]} and values {TEST_STRINGS_VALUES[pos]}")
            print(test_map.put(TEST_STRINGS_KEYS[pos], TEST_STRINGS_VALUES[pos]))
        self.test_map=test_map

    def test_insert_full(self):
        test_map=self.test_map
        self.assertIsNone(test_map.put("HopHey", "Nothing"))

    def test_empty_get(self):
        map_empty=NativeDictionary(7)
        self.assertIsNone((map_empty.get("Empty")))