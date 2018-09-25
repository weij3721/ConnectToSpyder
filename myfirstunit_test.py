# -*- coding: utf-8 -*-
"""
Created on Tue Sep 25 22:54:29 2018

@author: weij3721
"""

#my first python unit test

#def calculator_add(x,y):
#   z = x + y
#   return z

from firstSpyderScript import calculator_add
    
def test_answer():
    assert calculator_add(1,3) == 4
    