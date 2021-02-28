#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 00:28:00 2021

@author: jamesdoucette
"""
import unittest
from linked_list import ListNode

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
        
        