# -*- coding: utf-8 -*-
"""
There is a building of 100 floors. If an egg drops from the Nth floor or above,
it will break. If it's dropped from any floor below, it will not break. You're
given two eggs. Find N, while minimizing the number of drops for the worse 
case.

ANSWER:
        
    The goal is to keep the number of drops of the eggs as consistent as
    possible whether Egg #1 breaks on the first or last drop. This means that:
   
        num_drops(Egg #1) + num_drops(Egg #2) = constant
              
    regardless of where Egg #1 breaks.
    
    Apply "worst-case (load) balancing". Egg #1 must start at floor x, then go
    up by x-1 floors, then x-2 floors, etc until it reaches floor 100.
        
        100 = x + (x-1) + (x-2) + ... + 1
            = sum(x-i for i in range(x))        
            = x(x+1)/2
            
        x = -1/2 + 3*sqrt(89)/2, -3*sqrt(89)/2 - 1/2
          ~ 13.65, -14.65

    Obviously the rate should be an integer so we'll pick the positive root 
    and round up, so x = 14.

    To generalize to different building sizes solve:
        
        x(x+1)/2 = # of floors

@author: Victor Cannestro
"""

breakingPoint = 15


def setBreakingPoint(newPoint: int):
    breakingPoint = newPoint

def getBreakingPoint() -> int:
    return breakingPoint

def makeDrop():
    '''
    Returns
    -------
    func
        Returns the `drop(floor)` function. The free variable `countDrops` 
        is retained in the closure of `makeDrop()` allowing `drop(floor)` to
        access it as a nonlocal variable. The closure extends the scope of 
        `makeDrop` to included the binding for `countDrops`. See the following
        attributes for useful information:
        .__code__.co_varnames
        .__code__.co_freevars
        .__closure__[0].cell_contents
    '''
    countDrops = 0
    def drop(floor: int) -> bool:
        '''
        Parameters
        ----------
        floor : int
            The number of floors to drop the egg from.

        Returns
        -------
        bool
            Whether the egg broke or not.
        '''
        global breakingPoint
        nonlocal countDrops
        countDrops += 1
        return floor >= breakingPoint   
    return drop

def findBreakingPoint(floors: int) -> int:
    '''
    Parameters
    ----------
    floors : int
        The number of (above ground) floors in the building.

    Returns
    -------
    int
        The breaking point floor, if it is exists. Else, return -1 because the
        egg did not break.
    '''
    interval = 14
    prev = 0
    egg1 = interval
    drop = makeDrop()
    
    # Drop egg1 at decreasing intervals
    while not drop(egg1) and egg1 <= floors:
        interval -= 1
        prev = egg1
        egg1 += interval
        
    egg2 = prev + 1
    # Drop egg2 at 1 unit increments (i.e. linear seach)
    while egg2 < egg1 and egg2 <= floors and not drop(egg2):
        egg2 += 1
    
    # If egg2 didn't break, return -1
    return -1 if egg2 > floors else egg2


if __name__ == "__main__":
    num_floors = 100
    ans = findBreakingPoint(num_floors)
    print(ans)
    print(getBreakingPoint())