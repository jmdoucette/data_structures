import unittest
from data_structs import HashMap,OAMap


class HashMapTests(unittest.TestCase):
    def test(self):
        h = HashMap()
        self.assertEqual(len(h),0)
        
        h[0]=5
        h[1]=4
        self.assertEqual(h[0],5)
        self.assertEqual(h[1],4)
        self.assertEqual(len(h),2)
        
        h[2]=5
        h[0]=0
        self.assertEqual(h[0],0)
        self.assertEqual(h[2],5)
        self.assertEqual(len(h),3)
        self.assertEqual(0 in h,True)
        self.assertEqual(1 in h,True)
        self.assertEqual(2 in h,True)
        self.assertEqual(3 in h, False)
        
        h[2]=5
        h.pop(2)
        self.assertEqual(2 in h, False)
        self.assertEqual(0 in h, True)
        self.assertEqual(len(h), 2)
        
        
class OAMapTests(unittest.TestCase):
    def test(self):
        h = OAMap()
        self.assertEqual(len(h),0)
        
        h[0]=5
        h[1]=4
        self.assertEqual(h[0],5)
        self.assertEqual(h[1],4)
        self.assertEqual(len(h),2)
        
        h[2]=5
        h[0]=0
        self.assertEqual(h[0],0)
        self.assertEqual(h[2],5)
        self.assertEqual(len(h),3)
        self.assertEqual(0 in h,True)
        self.assertEqual(1 in h,True)
        self.assertEqual(2 in h,True)
        self.assertEqual(3 in h, False)
        
        h[2]=5
        h.pop(2)
        self.assertEqual(2 in h, False)
        self.assertEqual(0 in h, True)
        self.assertEqual(len(h), 2)

