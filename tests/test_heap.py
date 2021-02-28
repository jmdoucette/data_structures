#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 01:23:26 2021

@author: jamesdoucette
"""
import unittest
from heap import Heap


def is_heap(h,i):
    lchild = h.lchild(i)
    rchild = h.rchild(i)
    if lchild < len(h):
        if h.get_key(i)>h.get_key(lchild):
            return False
        elif not is_heap(h,lchild):
            return False
    if rchild < len(h):
        if h.get_key(i)>h.get_key(rchild):
            return False
        elif not is_heap(h,rchild):
            return False
    return True


class HeapTests(unittest.TestCase):  
    def test_initialization(self):
        h0=Heap([[1,0],[5,1],[4,2],[0,3]])
        self.assertEqual(is_heap(h0,0),True)
        
        h1=Heap([[1,0],[5,1],[4,2],[0,3],[-1,4],[-8,5],[10,6],[10,7]])
        self.assertEqual(is_heap(h1,0),True)
        
        h2=Heap([[1,0],[5,1],[4,2],[0,3]],lambda x:-x)
        self.assertEqual(is_heap(h2,0),True)
        
        h3=Heap([[1,0],[5,1],[4,2],[0,3],[-1,4],[-8,5],[10,6],[10,7]],lambda x:-x)
        self.assertEqual(is_heap(h3,0),True)
        
        
    def test_operations(self):
        h = Heap([])
        h.insert([4,0])
        h.insert([7,1])
        h.insert([1,2])
        h.insert([3,3])
        self.assertEqual(h.get_min(),[1,2])
        self.assertEqual(is_heap(h,0),True)
        
        
        h.insert([-1,4])
        h.insert([8,5])
        h.insert([0,6])
        h.insert([5,7])
        self.assertEqual(h.get_min(),[-1,4])
        self.assertEqual(h.extract_min(),[-1,4])
        self.assertEqual(h.get_min(),[0,6])
        self.assertEqual(h.extract_min(),[0,6])
        self.assertEqual(h.extract_min(),[1,2])
        self.assertEqual(is_heap(h,0),True)
        
        
        h.insert([0,8])
        h.update_key(3,-2)
        self.assertEqual(h.get_min(),[-2,3])
        h.update_key(5,100)
        h.update_key(5,-1)
        self.assertEqual(h.extract_min(),[-2,3])
        self.assertEqual(h.extract_min(),[-1,5])
        self.assertEqual(is_heap(h,0),True)
        
        
        h.update_key(1,2)
        h.update_key(8,3)
        self.assertEqual(h.get_min(),[2,1])
        self.assertEqual(is_heap(h,0),True)
        
    def test_max_operations(self):
        h = Heap([],lambda x:-x)
        h.insert([4,0])
        h.insert([7,1])
        h.insert([1,2])
        h.insert([3,3])
        self.assertEqual(h.get_min(),[7,1])
        self.assertEqual(is_heap(h,0),True)
        self.assertEqual(h.extract_min(),[7,1])
        
        h.update_key(2,10)
        self.assertEqual(h.extract_min(),[10,2])
        self.assertEqual(is_heap(h,0),True)
        
