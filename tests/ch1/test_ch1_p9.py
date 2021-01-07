# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 21:40:56 2021

@author: Victor Cannestro
"""

from src.ch1.p9_string_rotation import isRotation

class TestBasicCompression(object):
    ''''''
    def test_noEffect(self):
        s1 = "How now" # Compresses to "H1o1w1 1n1o1w1"
        s2 = ""
        assert isRotation(s1,s2) == "How now"
        
    def test_normalCase(self):
        s1 = "oooobeeee"
        s2 = ""
        assert isRotation(s1,s2) == "How now"
        
    def test_sameLength(self):
        s1 = "ttccaa" # Compresses to  "t2c2a2"
        s2 = ""
        assert isRotation(s1,s2) == "How now"
        
    def test_longer(self):
        s1 = "hubba" # "h1u1b2a1" is longer
        s2 = ""
        assert isRotation(s1,s2) == "How now"
        
    def test_empty(self):
        s1 = ""
        assert isRotation(s1,s1) == ""