from src.Queue.queue_circle import circle_queue
from src.Queue.queue_stacks import QueueStacks
import unittest

class TestCircle(unittest.TestCase):
    def test_default(self):
        q=QueueStacks()
        for i in range(1,10):
            q.enqueue(i)
        
        circle_queue(q, 3)
        
        self.assertEqual(q.get_head(),4, "4 is in the head")
        self.assertEqual(q.get_tail(),3, "3 is in the tail")
