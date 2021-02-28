import unittest
from data_structs import UnionFind

class UnionFindTests(unittest.TestCase):
    def test(self):
        uf=UnionFind()
        for i in range(8):
            uf.add(i)
        self.assertEqual(uf.same_component(0,2),False)
        self.assertEqual(uf.same_component(0,2),False)
        self.assertEqual(uf.same_component(4,0),False)
        
        uf.union(2,4)
        self.assertEqual(uf.same_component(2,4),True)
        
        uf.union(2,4)
        self.assertEqual(uf.same_component(4,2),True)
        
        uf.union(2,6)
        self.assertEqual(uf.same_component(2,6),True)
        self.assertEqual(uf.same_component(6,4),True)
        
        uf.union(0,7)
        uf.union(5,0)
        self.assertEqual(uf.same_component(5,2),False)
        self.assertEqual(uf.same_component(6,4),True)
        
        uf.union(5,6)
        uf.union(1,3)
        self.assertEqual(uf.same_component(7,2),True)
        self.assertEqual(uf.same_component(1,3),True)
        self.assertEqual(uf.same_component(1,7),False)
        self.assertEqual(uf.same_component(3,0),False)
    
