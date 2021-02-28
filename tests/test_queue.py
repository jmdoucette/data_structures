import unittest
from data_structs import Queue

class QueueTests(unittest.TestCase):
    def test(self):
        q=Queue()
        self.assertEqual(len(q),0)
        
        q.enqueue(3)
        self.assertEqual(q.front(),3)
        self.assertEqual(len(q),1)
        
        q.enqueue(2)
        q.enqueue(7)
        q.enqueue(2)
        self.assertEqual(q.front(),3)
        self.assertEqual(len(q),4)
            
        self.assertEqual(q.dequeue(),3)
        self.assertEqual(q.dequeue(),2)
        self.assertEqual(len(q),2)

