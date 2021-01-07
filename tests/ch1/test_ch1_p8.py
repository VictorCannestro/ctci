# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 19:17:49 2021

@author: Victor Cannestro
"""

from src.ch1.p8_zero_matrix import setZeros

class TestSetZeros(object):
    ''''''
    def test_one(self):
        matrix = [[1]]
        assert setZeros(matrix) == [[1]]
        
    def test_eye(self):
        matrix = [[1,0,0,0,0,0],
                  [0,1,0,0,0,0],
                  [0,0,1,0,0,0]]
        assert setZeros(matrix) == [[0,0,0,0,0,0],
                                    [0,0,0,0,0,0],
                                    [0,0,0,0,0,0]]
        
    def test_fat(self):
        matrix = [[1,0,3,0],
                  [1,2,4,5]]
        assert setZeros(matrix) == [[0,0,0,0],
                                    [1,0,4,0]]
        
    def test_skinny(self):
        matrix = [[1,0],
                  [1,2],
                  [1,3],
                  [1,4]]
        assert setZeros(matrix) == [[0,0],
                                    [1,0],
                                    [1,0],
                                    [1,0]]