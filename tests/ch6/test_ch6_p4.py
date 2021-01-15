# -*- coding: utf-8 -*-
"""
ANSWER:
    
    It is easier to think of the converse problem: in which cases will the 
    ants NOT collide. Here I will lay out two arguments to determine the 
    probability.
    
    1) SET THEORY ARGUMENT: Let's start by defining the events of interest and 
                            their respective probabilities: 
                         
    A = {The ants collide}  
    A^c = {The ants do not collide}
    
    P[A^c] = P[({A1 CCW} and {A2 CCW} and {A3 CCW}) U ({A1 CW} and {A2 CW} and {A3 CW}))]
           = P[{A1 CCW} and {A2 CCW} and {A3 CCW}] + P[{A1 CW} and {A2 CW} and {A3 CW}]   Since the events are disjoint
           = P[{A1 CCW}]P[{A2 CCW}]P[{A3 CCW}] + P[{A1 CCW}]P[{A2 CCW}]P[{A3 CCW}]        Since the ants are independent     
           = (p)(p)(p) + (p)(p)(p)
           = 2*p^3.
           
    P[A] = 1 - P[A^c]      Since all probs must sum to 1
         = 1 - 2*p^3
         = 1 - 2*(1/2)^3   Since they pick a direction with equal prob
         = 3/4. 
                       
    2) COMBINATORIAL ARGUMENT: There are only 2 cases: all are traveling CCW or 
                               all are traveling CW. Now all that's left to 
    determine the probability is to count the number of possible paths the 
    ants could take:                            
               
        N = (2 choose 1)*(2 choose 1)*(2 choose 1)
        = 2*2*2
        = 8.
        
    Thus the probability is the division of N_ac / N:
        
        P[A^c] = 2/8
               = 1/4.
               
        P[A] = 1 - 1/4
             = 3/4.
        
    Generalizing to n ants on an n vertex polygon yields an even smaller 
    probability:
        
        P[A] = 1 - 2/2^n
             = 1 - (1/2)^(n-1).

@author: Victor Cannestro
"""
import pytest
from src.ch6.p4_ants_on_a_triangle import estimateAntProb, calcAntProb


class TestCalcAntProb(object): 
    def test_Ac(self):
        _1, _2, calc = calcAntProb()
        ans = {(0,0,0),(1,1,1)}
        message = f"Expected {ans} but got {calc}"
        assert calc == ans, message
        
    def test_U(self):
        _1, calc, _2 = calcAntProb()
        ans = {(0,0,1),(0,1,0),(1,0,0),(1,1,0),(1,0,1),(0,1,1),(0,0,0),(1,1,1)}
        message = f"Expected {ans} but got {calc}"
        assert calc == ans, message
        
    def test_prob(self):
        calc, _1, _2 = calcAntProb()
        ans = 0.75
        tol = 0.01
        message = f"Expected {ans} but got {calc}"
        assert pytest.approx(calc, tol) == ans, message


class TestEstimateAntProb(object):
    n = [3, 5, 10]
    answers = [3/4, 15/16, 511/512]
    test_data = zip(n, answers)
    @pytest.mark.parametrize("n, ans", test_data)        
    def test_prob(self, n: int, ans: float):
        tol = 0.1
        calc = estimateAntProb(n)
        message = f"Expected {ans} but got {calc}"
        assert pytest.approx(calc, tol) == ans, message