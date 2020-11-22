from src.Stack.brackets import is_balanced
from src.Stack.stack_linked_list import Stack

import unittest

class TestBrackets(unittest.TestCase):
    def test_balanced_string(self):
        self.assertTrue(is_balanced('(())'), "String (()) is balanced")
    def test_balanced_string_complicated(self):
        
        string='(()((())()))'
        self.assertTrue(is_balanced(string), f"String {string} is balanced")
    def test_unbalanced_string(self):
        string='(()()(()'
        self.assertFalse(is_balanced(string), f"String {string} is unbalanced")
    
    def test_empty(self):
        string=''
        with self.assertRaises(Exception):
            is_balanced(string)
        #self.assertFalse(is_balanced(string), f"String {string} is unbalanced")
    
    def test_custom_string(self):
        string="asdfasdf"
        with self.assertRaises(Exception):
            is_balanced(string)