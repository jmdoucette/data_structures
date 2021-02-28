import unittest
from data_structs import HashSet, OASet


class HashSetTests(unittest.TestCase):
    def test(self):
        s = HashSet()
        self.assertEqual(len(s),0)
        
        s.add(5)
        s.add(5)
        self.assertEqual(len(s),1)
        self.assertEqual(5 in s, True)
        self.assertEqual(6 in s, False)
        
        s.add(10)
        s.add(15)
        s.remove(5)
        self.assertEqual(10 in s, True)
        self.assertEqual(5 in s, False)
        self.assertEqual(len(s),2)
        
        s.add(10)
        s.add(1)
        s.add(2)
        s.add(3)
        s.add(4)
        self.assertEqual(5 in s, False)
        self.assertEqual(4 in s, True)
        self.assertEqual(len(s),6)
        self.assertEqual(s.capacity,8)
        
class OASetTests(unittest.TestCase):
    def test(self):
        s = OASet()
        self.assertEqual(len(s),0)
        
        s.add(5)
        s.add(5)
        self.assertEqual(len(s),1)
        self.assertEqual(5 in s, True)
        self.assertEqual(6 in s, False)
        
        s.add(10)
        s.add(15)
        s.remove(5)
        self.assertEqual(10 in s, True)
        self.assertEqual(5 in s, False)
        self.assertEqual(len(s),2)
        
        s.add(10)
        s.add(1)
        s.add(2)
        s.add(3)
        s.add(4)
        self.assertEqual(5 in s, False)
        self.assertEqual(4 in s, True)
        self.assertEqual(len(s),6)
        self.assertEqual(s.capacity,32)