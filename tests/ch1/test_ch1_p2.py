# -*- coding: utf-8 -*-
"""
Created on Mon Jan  4 20:35:27 2021

@author: Victor Cannestro
"""

from src.ch1.p2_permutation import isPermutation

class TestIsPermutation(object):
    ''''''
    def test_one(self):
        s1 = "How now brown cow"
        s2 = "woc nworb won woH"
        assert isPermutation(s1,s2) == True
        
    def test_two(self):
        s1 = "salad taco"
        s2 = "taco salad"
        assert isPermutation(s1,s2) == True
        
    def test_same(self):
        s1 = "ooooooo"
        assert isPermutation(s1,s1) == True
        
    def test_differentLengths1(self):
        s1 = "goose"
        s2 = "soge"
        assert isPermutation(s1,s2) == False
        
    def test_differentLengths2(self):
        s1 = "How now brown cow"
        s2 = "moo"
        assert isPermutation(s1,s2) == False
        
    def test_empty(self):
        s1 = ""
        s2 = ""
        assert isPermutation(s1,s2) == False