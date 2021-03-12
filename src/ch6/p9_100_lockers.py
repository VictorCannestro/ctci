# -*- coding: utf-8 -*-
"""
There are 100 closed lockers in a hallway. A man begins by opening all 100 
lockers. Next, he closes every second locker. Then, on his third pass, he 
toggles every third locker (closes if if it is open or opens it if it is 
closed). This process continues for 100 passes, such that on each pass i, the
man toggles every ith locker. After his 100th pass in the hallway, in which he
toggles only locker #100, how many lockers are open?

@author: Victor Cannestro
"""

def closeLockers(n: int) -> int:
    '''
    Parameters
    ----------
    n : int
        The total number of lockers to consider.

    Returns
    -------
    int
        The number of lockers left open after toggling the ith locker over
        2 to n passes, assuming all lockers are open on the 1st pass. This is
        also the number of perfect squares whose squares are bounded by n.
    '''
    # Initialize all lockers to OPEN = 1
    lockers = [True]*n
    for i in range(2, n+1): # Toggle every ith locker
        for j in range(i, n+1, i):
            lockers[j-1] = not lockers[j-1] 
    return sum(lockers)


if __name__ == "__main__":
    print(closeLockers(50))