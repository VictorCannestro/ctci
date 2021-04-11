# -*- coding: utf-8 -*-
"""
- You have 1000 bottles of soda, and exactly one is poisoned. 

- You have 10 test strips which can be used to detect poison. A single drop of 
  poison will turn the test strip positive permanently. 

- You can put any number of drops on a single test strip at once and you can 
  reuse a test strip as many times as you'd like (as long as the results are 
  negative). 

- However, you can only run tests once per day and it takes seven days to 
  return a result. 

How would you figure out the poisoned bottle in as few days as possible. Write
code to simulate your approach.

@author: Victor Cannestro
"""
import numpy as np
from typing import List, Tuple


class Bottle:
    def __init__(self, id_val: int):
        self.ID = id_val
        self.isPoisoned = False # Make unpoisoned by default

    def __str__(self) -> str:
        return str(f"Bottle {self.ID}")
    
    def setIsPoisoned(self, newStatus: bool):
        self.isPoisoned = newStatus

    # Here for throroughness, though somewhat redundant in this implementation
    def getID(self) -> int:
        return self.ID
    
    def getStatus(self) -> bool:
        return self.isPoisoned


def generateBottles(N: int) -> Tuple:
    '''
    Parameters
    ----------
    N : int
        The number of bottles to consider.

    Returns
    -------
    Tuple
        The index of the poisoned bottle; A list of N Bottle objects where 
        exactly one is poisoned while the remaining N-1 are not.
    '''
    # Create a random index for the single poisoned bottle
    idx = np.random.randint(low=0, high=N, size=1)[0]
    # Model N Bottles as indicator variables of restricted visibility
    bottles = [Bottle(i) for i in range(N)]
    # Mark off the poisoned bottle
    bottles[idx].setIsPoisoned(True)
    return idx, bottles


def chunks(lst, n):
    """Helper Function: Yield successive n-sized chunks from lst."""
    chunky = []
    for i in range(0, len(lst), n):
        chunky.append(lst[i:i + n])
    return chunky

        
def useTestStrip(testBin) -> int:
    '''This is available to us as a black box test via the Test Strips.'''
    testResults = 0
    for bottle in testBin:
        testResults += bottle.getStatus() 
    return testResults


def findPoisonedSimple(bottles: List) -> int:
    '''
    Parameters
    ----------
    bottles : List
        A list of N indicator variables where exactly one value is 1 while 
        the remaining values are 0s.

    Returns
    -------
    int
        Finds the index of the poisoned sample. 
    '''
    testStrips = 10   
    subset = bottles
    bins = [100, 10, 2, 1]
    for binSize in bins:
        binnedBottles = chunks(subset, binSize)
        testResults = []
        # Run a test for each strip 
        for i in range(testStrips):
            if i == len(binnedBottles): # Case of more strips than bins
                break
            testBin = binnedBottles[i]
            testResults.append(useTestStrip(testBin))  
        if sum(testResults) > 0: # A bottle in this test bin is poisoned
            testStrips -= 1
            subset = binnedBottles[testResults.index(1)] # Focus on this bin
        else:
            subset = binnedBottles[-1]

    print(f"The number of days required to find the poisoned bottle is {7*(10-testStrips)}.")       
    return subset[0].getID()
    

if __name__ == "__main__":
    n = 1000
    idx, bottles = generateBottles(n)
    calc = findPoisonedSimple(bottles)
    print(f"Expected index: {idx}\nCalculated index: {calc}")