#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:47:13 2021

@author: jamesdoucette
"""
import unittest
from stack import Stack

class StackTests(unittest.TestCase):
    def test(self):
        s=Stack()
        self.assertEqual(len(s),0)
        
        s.push(3)
        self.assertEqual(s.top(),3)
        self.assertEqual(len(s),1)
        
        s.push(2)
        s.push(7)
        s.push(2)
        self.assertEqual(s.top(),2)
        self.assertEqual(len(s),4)
        
        self.assertEqual(s.pop(),2)
        self.assertEqual(s.pop(),7)
        self.assertEqual(len(s),2)