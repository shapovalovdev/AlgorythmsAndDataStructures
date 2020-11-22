import unittest
from src.NativeDictionary.map import NativeDictionary

class TestNativeDictionaryPositive(unittest.TestCase):
    def setUp(self):
        test_map = NativeDictionary(17)
        TEST_STRINGS_KEYS = ["name", "birthday", "profession", "institute", "hobby"]
        TEST_STRINGS_VALUES = ["Irina", "16.09.1991", "Programmer", "MSU", "cats"]
        for pos in range(len(TEST_STRINGS_KEYS)):
            print(f"hash_fun of {TEST_STRINGS_KEYS[pos]} is {test_map.hash_fun(TEST_STRINGS_KEYS[pos])}")
            print(f"{pos} string of keys {TEST_STRINGS_KEYS[pos]} and values {TEST_STRINGS_VALUES[pos]}")
            print(test_map.put(TEST_STRINGS_KEYS[pos], TEST_STRINGS_VALUES[pos]))
        self.test_map=test_map





    # Test1:
    # добавление значения по новому ключу с проверками что записалось
    def test_add_new_key(self):
        test_map=self.test_map
        test_map.put("sex", "female")
        self.assertEqual(test_map.get("sex"),"female", "Check if sex female or not")

    # Test2:
    # добавление значения по уже существующему ключу с проверками что записалось,
    def test_the_same_key(self):
        test_map=self.test_map
        print("Run test the same key")
        self.assertEqual(test_map.get("institute"),"MSU", "Check if instite is MSU")
        test_map.put("hobby", "dogs")
        print(f"Check if institute is {test_map.get('hobby')}")
        self.assertEqual(test_map.get("hobby"), "dogs", f"Check if hobby is  dogs")
    # Test3:
    # проверка присутствующего ключа
    def test_existing_key(self):
        test_map=self.test_map
        test_map.put("Hop", "Hey")
        self.assertEqual(test_map.is_key("hobby"),True, "Check if institute is key or not")
        self.assertEqual(test_map.is_key("Hey"), False, "Check if institute is key or not")
        self.assertEqual(test_map.is_key("Hop"), True, "Check if institute is key or not")

    # Test4:
    # и отсутствующего ключа,
    def test_not_existing_key(self):
        test_map=self.test_map
        self.assertEqual(test_map.is_key("AbirValg"), False, "Check if abirvalg is key or not")

    # Test5:
    # извлечение значения по существующему
    def test_get_value_existing(self):
        test_map=self.test_map
        self.assertEqual(test_map.get("profession"), "Programmer", "Check if profession is programmer")

    def test_get_value_not_existing(self):
        test_map=self.test_map
        self.assertIsNone(test_map.get("AbirValg"), "Abirvalg is None")




    # Test6:
    # и отсутствующему ключу.