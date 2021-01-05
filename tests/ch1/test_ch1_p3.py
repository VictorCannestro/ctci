# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 21:12:41 2021

@author: Victor Cannestro
"""

from src.ch1.p3_URLify import urlify

class TestURLify(object):
    ''''''
    def test_one(self):
        s1 = "How now brown cow"
        assert urlify(s1) == "How%20now%20brown%20cow"
        
    def test_spaceAtEnd(self):
        s1 = "salad taco "
        assert urlify(s1) == "salad%20taco"
        
    def test_spaceAtBeginning(self):
        s1 = " ooooooo"
        assert urlify(s1) == "ooooooo"
        
    def test_manySpaces(self):
        s1 = "g o o s e"
        assert urlify(s1) == "g%20o%20o%20s%20e"
        
    def test_empty(self):
        s1 = ""
        assert urlify(s1) == ""