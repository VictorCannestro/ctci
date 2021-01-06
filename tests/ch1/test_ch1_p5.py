# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 22:35:21 2021

@author: Victor Cannestro
"""

from src.ch1.p5_one_away import oneEditAway

class TestOneEditAway(object):
    ''''''
    def test_one(self):
        s1 = "How now"
        s2 = "How now"
        assert oneEditAway(s1,s2) == True
        
    def test_itself(self):
        s1 = "tacocat"
        assert oneEditAway(s1,s1) == True
        
    def test_insert(self):
        s1 = "taccat"
        s2 = "tacocat"
        assert oneEditAway(s1,s2) == True
        
    def test_replace(self):
        s1 = "tacocut"
        s2 = "tacocat"
        assert oneEditAway(s1,s2) == True
        
    def test_length2Big(self):
        s1 = "taco"
        s2 = "tacocat"
        assert oneEditAway(s1,s2) == False
        
    def test_empty(self):
        s1 = ""
        assert oneEditAway(s1,s1) == True