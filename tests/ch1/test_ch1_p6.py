# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:51:28 2021

@author: Victor Cannestro
"""

from src.ch1.p6_string_compression import basicCompression

class TestBasicCompression(object):
    ''''''
    def test_noEffect(self):
        s1 = "How now" # Compresses to "H1o1w1 1n1o1w1"
        assert basicCompression(s1) == "How now"
        
    def test_normalCase(self):
        s1 = "oooobeeee"
        assert basicCompression(s1) == "o4b1e4"
        
    def test_sameLength(self):
        s1 = "ttccaa" # Compresses to  "t2c2a2"
        assert basicCompression(s1) == "ttccaa"
        
    def test_longer(self):
        s1 = "hubba" # "h1u1b2a1" is longer
        assert basicCompression(s1) == "hubba"
        
    def test_empty(self):
        s1 = ""
        assert basicCompression(s1) == ""