import unittest
from data_structs import ListNode

class ListNodeTests(unittest.TestCase):
    def test_contains(self):
        l=ListNode(5,ListNode(3,ListNode(7,None)))
        self.assertEqual(5 in l,True)
        self.assertEqual(3 in l,True)
        self.assertEqual(7 in l,True)
        self.assertEqual(1 in l,False)
        
    def test_eq(self):
        l1=ListNode(5,ListNode(3,ListNode(7,None)))
        l2=ListNode(3,ListNode(7,None))
        self.assertEqual(l1==l2,False)
        
        l2=ListNode(5,l2)
        self.assertEqual(l1==l2,True)
        
    def test_iter(self):
        l=ListNode(5,ListNode(3,ListNode(7,None)))
        check=[]
        for node in l:
            check.append(node.val)
        self.assertEqual(check,[5,3,7])
        
        