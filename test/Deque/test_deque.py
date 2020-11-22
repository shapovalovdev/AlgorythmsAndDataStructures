
from src.Deque.deque_stacks import DequeStacks
from src.Deque.deque_scratch import Deque
from src.Deque.palindrome_deque import is_palindrome
import unittest

class TestDeque(unittest.TestCase):
    #testing endeque
    def setUp(self):
        self.deques={}
        test_deque1=Deque()
        #test_deque2=DequeStacks()        
        self.deques["DequeDefault"]=test_deque1
        #self.deques["DequeStacks"]=test_deque2
        

    def test_deque_empty_list(self):           
        for q_name,q in self.deques.items():
            with self.subTest(q_name):
                self.assertIsNone(q.removeFront(), f"In deque {q_name} Remove from Front, it should return None")
                self.assertIsNone(q.removeTail(), f"In deque {q_name} Remove fromt Tail nothing, it should return None")
                self.assertIsNone(q.getFront(), f"In deque {q_name} Front should be None")
                self.assertIsNone(q.getTail(), f"In deque {q_name} Tail should be None")
                self.assertEqual(q.size(),0, f"In  deque {q_name} the size is 0")
    
    def test_deque_default_add(self):
        for q_name,q in self.deques.items():
            with self.subTest(q_name):                
                self.assertEqual(q.size(),0, f"In  deque {q_name} the size is 0")
                v1=7432
                v2=4123
                v3=-123
                v4=332
                q.addFront(v1)
                self.assertEqual(q.size(),1, f"In  deque {q_name} the size is 1")
                self.assertEqual(q.getFront(),v1, f"In  deque {q_name} the size is 7432")
                self.assertEqual(q.getTail(),v1, f"In  deque {q_name} the tail is 7432")
                q.addTail(v2)
                self.assertEqual(q.size(),2, f"In  deque {q_name} the size is 2")
                self.assertEqual(q.getFront(),v1, f"In  deque {q_name} the size is {v1}")
                self.assertEqual(q.getTail(),v2, f"In  deque {q_name} the tail is {v2}")
                q.addTail(v3)
                q.addTail(v4)
                self.assertEqual(q.size(),4, f"In  deque {q_name} the size is 4")
                self.assertEqual(q.getTail(), v4, f"In  deque {q_name} dedeque {v4}" )
                self.assertEqual(q.getFront(), v1, f"In  deque {q_name} dedeque {v1}" )
                self.assertEqual(q.removeFront(), v1, f"In  deque {q_name} dedeque {v1}" )
                self.assertEqual(q.size(),3, f"In  deque {q_name} the size is 3")
                self.assertEqual(q.removeTail(), v4, f"In  deque {q_name} dedeque {v4}" )
                self.assertEqual(q.size(),2, f"In  deque {q_name} the size is 2")
                self.assertEqual(q.removeFront(), v2, f"In  deque {q_name} dedeque {v2}" )
                self.assertEqual(q.size(),1, f"In  deque {q_name} the size is 2")
                self.assertEqual(q.removeFront(), v3, f"In  deque {q_name} dedeque {v3}" )
                self.assertEqual(q.size(),0, f"In  deque {q_name} the size is 0")
                q.addTail(v2)
                self.assertEqual(q.size(),1, f"In  deque {q_name} the size is 0")
                self.assertEqual(q.getFront(), v2, f"In  deque {q_name} dedeque {v2}" )

    def test_palindrome_positive(self):
        test1="123321"
        test2="racecar"
        test3="фываавыф"
        test4="RR"
        test5="1"
        
        self.assertTrue(is_palindrome(test1))
        self.assertTrue(is_palindrome(test2))
        self.assertTrue(is_palindrome(test3))
        self.assertTrue(is_palindrome(test4))
        self.assertTrue(is_palindrome(test5))
        
    def test_palindrome_negative(self):
        test1="12531"
        test2="ImetSomeone"
        test3="Протвино"
        test4=""
        
        self.assertFalse(is_palindrome(test1))
        self.assertFalse(is_palindrome(test2))
        self.assertFalse(is_palindrome(test3))
        with self.assertRaises(Exception):
            is_palindrome(test4)
           



    def test_lof_of_removing_front_tail(self):
        for q_name,q in self.deques.items():
            with self.subTest(q_name):
                length=1000
                for i in range(0,length):
                    q.addFront(i)

                self.assertEqual(q.size(),length, f"In  deque {q_name} The size is {length}")
                for i in range(0,length):
                    check=q.removeTail()
                    self.assertEqual(check, i, f"In  deque {q_name} dedeque is {i}")
                    check_size=length-i-1
                    self.assertEqual(check_size, q.size(), f"In  deque {q_name} size is {check_size}")

    def test_lof_of_removing_tail_front(self):
        for q_name,q in self.deques.items():
            with self.subTest(q_name):
                length=1000
                for i in range(0,length):
                    q.addTail(i)

                self.assertEqual(q.size(),length, f"In  deque {q_name} The size is {length}")
                for i in range(0,length):
                    check=q.removeFront()
                    self.assertEqual(check, i, f"In  deque {q_name} dedeque is {i}")
                    check_size=length-i-1
                    self.assertEqual(check_size, q.size(), f"In  deque {q_name} size is {check_size}")

    # def test_lof_of_dedeque_with_additional_checks(self):
    #     for q_name,q in self.deques.items():
    #         with self.subTest(q_name):
    #             length=1000
    #             q.endeque(1)
    #             q.dedeque()
    #             q.dedeque()
    #             self.assertEqual(q.size(),0, f"In  deque {q_name} The size is 0")

    #             for i in range(0,length):
                        
    #                 q.endeque(i)
    #                 self.assertEqual(q.size(),i+1, f"In  deque {q_name} The size is {i+1}")
        

    #             self.assertEqual(q.size(),length,f"In  deque {q_name} The size is {length}")
    #             for i in range(0,length):
    #                 check=q.dedeque()
    #                 self.assertEqual(check, i, f"In  deque {q_name} dedeque is {i}")
    #                 check_size=length-i-1
    #                 self.assertEqual(check_size, q.size(), f"In  deque {q_name} size is {check_size}")


