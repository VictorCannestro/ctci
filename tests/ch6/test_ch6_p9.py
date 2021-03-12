# -*- coding: utf-8 -*-
"""
ANSWER:
    
    Let's start with a smaller version of this problem and see what 
    conclusions can be drawn from there. Let the number of lockers be N = 10.
    Then we'll follow the algorithm laid out in the problem statement:
        
        1st) Open all the lockers.
        2nd) Close every other locker.
        3rd) Toggle every 3rd locker.
        .
        .
        .
        10th) Toggle every 10th locker.
    
    For ease of notation we'll encode "Open" as "o" and "Closed" as "x".
    
    Locker  _ _ _ _ _ _ _ _ _ __ 
      #     1 2 3 4 5 6 7 8 9 10
    Pass
    1       o o o o o o o o o o
    2       o x o x o x o x o x
    3       o x x x o o o x x x
    4       o x x o o o o o x x
    5       o x x o x o o o x o
    6       o x x o x x o o x o
    7       o x x o x x x o x o
    8       o x x o x x x x x o
    9       o x x o x x x x o o
    10      o x x o x x x x o x
            1     4         9
            
    In conclusion, locker numbers 1,4, and 9 are left open by the end of the
    algorithm. This sequence defines the perfect squares up to locker number
    N. Therefore, the answer to this question is to count how many perfect 
    squares there are between 1 and N, inclusive. Between 1 and 100 there are
    10 perfect squares: 
        
    1**2 = 1
    2**2 = 4
    3**2 = 9
    4**2 = 16
    5**2 = 25
    6**2 = 36
    7**2 = 49
    8**2 = 64
    9**2 = 81
    10**2 = 100
        
@author: Victor Cannestro
"""

import pytest
from src.ch6.p9_100_lockers import closeLockers

class TestCloseLockers(object):
    N = range(10, 110, 10) 
    # The number of perfect squares whose squares are bounded by N.
    answers = [len([i for i in range(1,x) if i**2 <= x]) for x in N]
    
    @pytest.mark.parametrize("n, ans", zip(N, answers))
    def test_closeLockers(self, n: int, ans: int):
        calc = closeLockers(n)
        message = f"Expected {ans}, but got {calc}"
        assert calc == ans, message