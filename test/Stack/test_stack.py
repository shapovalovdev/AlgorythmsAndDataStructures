from src.Stack.stack_linked_list import Stack, Node
import unittest
class TestStack(unittest.TestCase):
    def test_stack_peek(self):
        stack=Stack()
        stack.push(77)
        stack.push(123)
        self.assertEqual(stack.peek(),123,"We should peek 123")
        self.assertEqual(stack.pop(),123, "We hsould pop 123")
        self.assertEqual(stack.peek(),77,"We should peek 77")
        self.assertEqual(stack.pop(),77,"We should pop 77")
        self.assertEqual(stack.size(),0)
        self.assertIsNone(stack.peek(), "peek is none" )  

    def test_push(self):
        pass
    
    def test_pop_one_element(self):
        stack=Stack()
        stack.push(1)
        stack.pop()
        self.assertEqual(stack.tail, None)
        self.assertEqual(stack.head, None)
        self.assertEqual(stack.size(),0)
    
    def test_pop_two_element(self):
        stack=Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(),2,"We should pop 2")
        self.assertEqual(stack.peek(),1)
        self.assertEqual(stack.size(),1)
        self.assertEqual(stack.pop(),1,"We should pop 1")
        self.assertEqual(stack.size(),0)
    
    def test_peek_empty(self):
        stack=Stack()
        self.assertIsNone(stack.peek(), "peek is none" )     
        