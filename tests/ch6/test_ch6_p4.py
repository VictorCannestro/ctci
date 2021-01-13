# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 19:30:01 2021

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