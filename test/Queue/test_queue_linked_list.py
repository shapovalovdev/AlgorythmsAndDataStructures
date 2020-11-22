from src.Queue.queue_linked_list import Queue
from src.Queue.queue_stacks import QueueStacks
import unittest

class TestQueue(unittest.TestCase):
    #testing enqueue
    def setUp(self):
        self.queues={}
        test_queue1=Queue()
        test_queue2=QueueStacks()
        self.queues["QueueDefault"]=test_queue1
        self.queues["QueueStacks"]=test_queue2
        

    def test_queue_empty_list(self):           
        for q_name,q in self.queues.items():
            with self.subTest(q_name):
                self.assertIsNone(q.dequeue(), f"In queue {q_name} It should be None")
                self.assertEqual(q.size(),0, f"In  queue {q_name} the size is 0")
    
    def test_dequeue_default(self):
        for q_name,q in self.queues.items():
            with self.subTest(q_name):                
                self.assertEqual(q.size(),0, f"In  queue {q_name} the size is 0")
                q.enqueue(123)
                self.assertEqual(q.size(),1, f"In  queue {q_name} the size is 1")
                q.enqueue(1000)
                q.enqueue(-123)
                self.assertEqual(q.size(),3, f"In  queue {q_name} the size is 3")
                self.assertEqual(q.dequeue(), 123, f"In  queue {q_name} dequeue 123" )
                self.assertEqual(q.dequeue(), 1000, f"In  queue {q_name} dequeue 1000" )
                self.assertEqual(q.dequeue(), -123, f"In  queue {q_name} dequeue -123" )
                self.assertEqual(q.size(),0, f"In  queue {q_name} the size is 0")

    def test_enqueue_lot(self):
        for q_name,q in self.queues.items():
            with self.subTest(q_name):
                length=1000
                q.enqueue(1)
                q.dequeue()
                q.dequeue()
                self.assertEqual(q.size(),0,f"In  queue {q_name} The size is 0")
                q.enqueue(1)
                self.assertEqual(q.size(),1,f"In  queue {q_name} The size is 1")
                for i in range(1,length):
                    q.enqueue(i)
                    self.assertEqual(q.size(),i+1, f"In  queue {q_name} The size is {i+1}")
                self.assertEqual(q.size(),length, f"In  queue {q_name} The size is {length}")


    def test_lof_of_dequeue(self):
        for q_name,q in self.queues.items():
            with self.subTest(q_name):
                length=1000
                for i in range(0,length):
                    q.enqueue(i)

                self.assertEqual(q.size(),length, f"In  queue {q_name} The size is {length}")
                for i in range(0,length):
                    check=q.dequeue()
                    self.assertEqual(check, i, f"In  queue {q_name} dequeue is {i}")
                    check_size=length-i-1
                    self.assertEqual(check_size, q.size(), f"In  queue {q_name} size is {check_size}")

    def test_lof_of_dequeue_with_additional_checks(self):
        for q_name,q in self.queues.items():
            with self.subTest(q_name):
                length=1000
                q.enqueue(1)
                q.dequeue()
                q.dequeue()
                self.assertEqual(q.size(),0, f"In  queue {q_name} The size is 0")

                for i in range(0,length):
                        
                    q.enqueue(i)
                    self.assertEqual(q.size(),i+1, f"In  queue {q_name} The size is {i+1}")
        

                self.assertEqual(q.size(),length,f"In  queue {q_name} The size is {length}")
                for i in range(0,length):
                    check=q.dequeue()
                    self.assertEqual(check, i, f"In  queue {q_name} dequeue is {i}")
                    check_size=length-i-1
                    self.assertEqual(check_size, q.size(), f"In  queue {q_name} size is {check_size}")


