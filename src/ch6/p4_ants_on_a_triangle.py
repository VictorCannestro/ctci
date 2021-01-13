# -*- coding: utf-8 -*-
"""
There are three ants on different vertices of a triangle. What is the
probability of collision (between any two or all of them) if they start walking
on the sides of the triangle? Assume that each ant randomly picks a direction 
with either direction being equally likely to be chosen, and that they walk at 
the same speed.

Similarly, find the probability of collision with n ants on an n vertex 
polygon.

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