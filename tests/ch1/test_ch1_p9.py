# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 21:40:56 2021

@author: Victor Cannestro
"""

from src.ch1.p9_string_rotation import isRotation, isRotationVer2

class TestIsRotation(object):
    ''''''
    def test_nomalCase1(self):
        s1 = "goosebumps" 
        s2 = "bumpsgoose"
        assert isRotation(s1,s2) == True
        
    def test_normalCase2(self):
        s1 = "tacocat"
        s2 = "goose"
        assert isRotation(s1,s2) == False
        
    def test_sameWord(self):
        s1 = "rotation" 
        assert isRotation(s1,s1) == True # Rotation of order 0
        
    def test_ambiguous(self):
        s1 = "vvvv" 
        s2 = "vvvv" # Could be a permutation instead of a rotation
        assert isRotation(s1,s2) == True
        
    def test_empty(self):
        s1 = ""
        assert isRotation(s1,s1) == False # By convention
        
        
class TestIsRotationVer2(object):
    ''''''
    def test_nomalCase1(self):
        s1 = "goosebumps" 
        s2 = "bumpsgoose"
        assert isRotationVer2(s1,s2) == True
        
    def test_normalCase2(self):
        s1 = "tacocat"
        s2 = "goose"
        assert isRotationVer2(s1,s2) == False
        
    def test_sameWord(self):
        s1 = "rotation" 
        assert isRotationVer2(s1,s1) == True # Rotation of order 0
        
    def test_ambiguous(self):
        s1 = "vvvv" 
        s2 = "vvvv" # Could be a permutation instead of a rotation
        assert isRotationVer2(s1,s2) == True
        
    def test_empty(self):
        s1 = ""
        assert isRotationVer2(s1,s1) == False # By convention