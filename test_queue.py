#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 31 14:48:02 2021

@author: jamesdoucette
"""
import unittest
from queue import Queue

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

