# -*- coding: utf-8 -*-
"""
ANSWER:
    
    Since we're given 10 test strips and 1000 bottles a fairly intuitive 
    approach would be to label the bottles #1-1000 and place them into bins of
    10. The algorithm procedes as follows:
        
        1) Split the bottles into bins of 10:
           1-100, 101-200, ..., 901-1000
            
           USABLE STRIPS: 10     
           BIN LENGTHS: 100
           TIME ELAPSED: 0 days
            
        2) Place a drop from each of the bottles onto it's respective test 
           strip and wait a week for the results. One of the bins will test 
           positive for poison so we'll have to toss that test strip.
           
           USABLE STRIPS: 9
           BIN LENGTHS: 100
           TIME ELAPSED: 7 days
        
        3) Next, we partition the positive bin of 100 into subsets of 10 bins,
           test 9 of those bins with the remaining test strips, and wait a week
           for the results. If all the tests are negative, then the untested 
           bin will contain the poisoned bottle. Again, we'll have to toss the
           positive test strip, if there is one.
    
           USABLE STRIPS: 8-9
           BIN LENGTHS: 10
           TIME ELAPSED: 14 days
    
        4) Next, we partition the positive bin of 10 bottles into subsets of 2
           bins each, costing a total of 5 test strips. We place a drop from 
           each of the bottles onto it's respective test strip and wait a week
           for the results. 
    
           USABLE STRIPS: 7-8
           BIN LENGTHS: 2
           TIME ELAPSED: 21 days
           
        5) Finally, we test the remaining two bottles with one test strip 
           each, wait a week for the results, and know with certainty 
           afterwards which of the 1000 bottles is poisoned.
           
           USABLE STRIPS: 6-7
           BIN LENGTHS: 1
           TIME ELAPSED: 28 days
           
@author: Victor Cannestro
"""
import pytest
from src.ch6.p10_poison import Bottle, generateBottles, findPoisonedSimple


# Done
class TestBottle(object):
    ids = [1, 2, 30]
    bottles = [Bottle(i) for i in ids]
    bottles[0].setIsPoisoned(True)
    statuses = [True, False, False]
    
    @pytest.mark.parametrize("b_id, bottle", zip(ids, bottles))
    def test___str__(self, b_id: int, bottle: Bottle):
        ans = f"Bottle {b_id}"
        calc = str(bottle)
        message = f"Expected {ans} but got {calc}"
        assert ans == calc, message
    
    @pytest.mark.parametrize("status, bottle", zip(statuses, bottles))
    def test_setStatus(self, status: bool, bottle: Bottle):
        calc = bottle.getStatus()
        message = f"Expected {status} but got {calc}"
        assert status == calc, message
        
        
class TestGenerateBottles(object):        
    def test_onePoisoned(self):
        ans = 1
        _, gen_bottles = generateBottles(12) 
        calc = sum(bottle.getStatus() for bottle in gen_bottles)
        message = "Expected 1 poisoned but got {calc}"
        assert ans==calc, message
        

class findSimple(object):    
    def test_completeFunctionality(self):
        ans, gen_bottles = generateBottles(12)
        calc = findPoisonedSimple(gen_bottles)
        message = "Expected {ans} but got {calc}"
        assert ans==calc, message