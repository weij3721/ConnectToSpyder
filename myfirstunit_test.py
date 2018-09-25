# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 22:54:29 2018

@author: weij3721
"""

#my first python unit test

def calculator_add(x,y):
    z = x + y
    return z
    
def test_answer():
    assert calculator_add(1,2) == 4
    