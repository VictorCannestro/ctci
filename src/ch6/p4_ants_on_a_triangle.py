# -*- coding: utf-8 -*-
"""
There are three ants on different vertices of a triangle. What is the
probability of collision (between any two or all of them) if they start walking
on the sides of the triangle? Assume that each ant randomly picks a direction 
with either direction being equally likely to be chosen, and that they walk at 
the same speed.

Similarly, find the probability of collision with n ants on an n vertex 
polygon.
   
@author: Victor Cannestro
"""
from typing import Tuple
import numpy as np


def calcAntProb() -> Tuple:
    '''
    Returns
    -------
    Tuple
        The probability of collision, possible outcomes, and outcomes leading 
        to a collision. Only works for the case of 3 ants as of now.
    '''
    Ac = {(0,0,0),(1,1,1)}
    outcomes = {(i,j,k) for i in [0,1] for j in [0,1] for k in [0,1]}
    A = outcomes - Ac
    return len(A)/len(outcomes), outcomes, Ac


def estimateAntProb(ants: int, N: int = 100000) -> float:
    '''
    Parameters
    ----------
    ants : int
        The number of ants to consider. It will also correspond to the number
        of vertices.

    Returns
    -------
    float
        An estimation of the probability of the ants colliding on an N vertex
        polygon. (Assuming there is one ant per vertex).
    '''
    N_Ac = 0
    for i in range(N):
        # All ants pick a direction and go
        outcome = np.random.binomial(1, 0.5, size=ants)
        if sum(outcome) in [0,ants]:
            N_Ac += 1
    return 1 - N_Ac / N


if __name__ == "__main__":
    prob, outs, event = calcAntProb()
    print(prob)
    print(event)
    print(outs)    
    print(estimateAntProb(3))