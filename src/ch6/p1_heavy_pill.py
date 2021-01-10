# -*- coding: utf-8 -*-
"""
You have 20 bottles of pills. 19 bottles have 1 gram pills, but one has pills
of weight 1.1 grams. Given a scale that provides an exact measurement, how 
would you find the heavy bottle? You can only use the scale once.

ANSWER:
    
    Let's sample different numbers of pills from each bottle that way we can
    differentiate between bottles (otherwise we wouldn't be able to tell them 
    apart): set s_1 = 1, s_2 = 2, ..., and s_20 = 20 pills. This information
    is known, however, we don't know the individual pill weights, w_i, of each 
    bottle. Then the measurement we record from using the scale once is:
        
        y_measurement = s_1*w_1 + s_2*w_2 + ... + s_19*w_19 + s_20*w_20 
                      = w_1 + 2*w_2 + ... + 19*w_19 + 20*w_20
                      = w_normal*(1+2+...+20) + (w_heavy - w_normal)*e
                      = w_normal*(1+2+...+20) + 0.1*x 
    
    where "x" is the number of heavy pills sampled. Since we sampled according
    to the pill bottle number, this is also the answer! Rearranging, we see 
    that:
        
        x = ( y_measurement - w_normal*(1+2+...+20) ) / (w_heavy - w_normal)
    
@author: Victor Cannestro
"""
from typing import List


def findOutlier(y: int, samples: List) -> float:
    '''
    Parameters
    ----------
    y : int
        The weight measured.
    samples : List
        The ith bottle had i samples taken from it.

    Returns
    -------
    float
        The pill bottle number of the outlier, indexed from 1.
    '''
    WEIGHT = 1.0
    EXTRA = 0.1
    return ( y - WEIGHT*sum(samples) ) / EXTRA


if __name__ == "__main__":
    N = 20
    y_measurement = 211.5
    bottleIDs = [i for i in range(1,N+1)]
    samples = [i for i in range(1,N+1)]
    idx = int(findOutlier(y_measurement, samples)) - 1
    print(f"The outlier is Bottle {bottleIDs[idx]}.")