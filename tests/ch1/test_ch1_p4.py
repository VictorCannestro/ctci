# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 21:28:28 2021

@author: Victor Cannestro
"""

from src.ch1.p4_palindrone_permutation import isPermutedPalindrone

class TestPermutedPalindrone(object):
    ''''''
    def test_one(self):
        s1 = "How now"
        assert isPermutedPalindrone(s1) == False
        
    def test_oddPalindrone(self):
        s1 = "tacocat"
        assert isPermutedPalindrone(s1) == True
        
    def test_evenPalindrone(self):
        s1 = "taccat"
        assert isPermutedPalindrone(s1) == True
        
    def test_repeatedLetter(self):
        s1 = "ooooo"
        assert isPermutedPalindrone(s1) == True
        
    def test_manySpaces(self):
        s1 = "g o o s e"
        assert isPermutedPalindrone(s1) == False
        
    def test_empty(self):
        s1 = ""
        assert isPermutedPalindrone(s1) == False