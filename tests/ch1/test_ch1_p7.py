# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 17:58:19 2021

@author: Victor Cannestro
"""

from src.ch1.p7_rotate_matrix import rotate, rotateInPlace

class TestBasicCompression(object):
    ''''''
    def test_one(self):
        matrix = [[1]]
        assert rotate(matrix) == [[1]]
        
    def test_two(self):
        matrix = [[1,2],
                  [3,4]]
        assert rotate(matrix) == [[2,4],
                                  [1,3]]
        
    def test_three(self):
        matrix = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]
        assert rotate(matrix) == [[3, 6, 9],
                                  [2, 5, 8], 
                                  [1, 4, 7]]
        
    def test_four(self):
        matrix = [[1,0,0,0],
                  [0,1,0,0],
                  [0,0,1,0],
                  [0,0,0,1]]
        assert rotate(matrix) == [[0,0,0,1],
                                  [0,0,1,0],
                                  [0,1,0,0],
                                  [1,0,0,0]]
        
        
class TestCompressionInPlace(object):
    ''''''
    def test_one(self):
        matrix = [[1]]
        assert rotateInPlace(matrix) == [[1]]
        
    def test_two(self):
        matrix = [[1,2],
                  [3,4]]
        assert rotateInPlace(matrix) == [[2,4],
                                         [1,3]]
        
    def test_three(self):
        matrix = [[1,2,3],
                  [4,5,6],
                  [7,8,9]]
        assert rotateInPlace(matrix) == [[3, 6, 9], 
                                         [2, 5, 8], 
                                         [1, 4, 7]]
        
    def test_four(self):
        matrix = [[1,0,0,0],
                  [0,1,0,0],
                  [0,0,1,0],
                  [0,0,0,1]]
        assert rotateInPlace(matrix) == [[0,0,0,1],
                                         [0,0,1,0],
                                         [0,1,0,0],
                                         [1,0,0,0]]

    def test_five(self):
        matrix = [[ 1, 2, 3, 4, 5],
                  [ 6, 7, 8, 9,10],
                  [11,12,13,14,15],
                  [16,17,18,19,20],
                  [21,22,23,24,25]]
        assert rotateInPlace(matrix) == [[5,10,15,20,25],
                                         [4,9,14,19,24],
                                         [3,8,13,18,23],
                                         [2,7,12,17,22],
                                         [1,6,11,16,21]]