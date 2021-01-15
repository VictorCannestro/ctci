# -*- coding: utf-8 -*-
"""
In the new post-apocalyptic world, the world queen is desperately concerned
about the birth rate. Therefore, she decrees that all families should ensure 
that they have one girl or else they face massive fines. If all families abide 
by this policy--that is, they have continue to have children until they have
one girl, at which point they immediately stop--what will the gender ratio of 
the new generation be? (Assume that the odds of someone having a boy or a girl
on any given pregnancy is equal). Solve this out logically and then write a 
computer simulation of it.

@author: Victor Cannestro
"""
import numpy as np


def approxBoysSeries(N: int) -> float:
    '''
    Parameters
    ----------
    N : int
        Number of families to consider.

    Returns
    -------
    float
        The sum of the number of boys weighted by corresponding probabilities.
    '''
    return sum(k/2**(k+1) for k in range(0,N+1))

    
def estimateRatio(fams: int) -> float:
    '''
    Parameters
    ----------
    fams : int
        Number of families to consider.

    Returns
    -------
    float
        The gender ratio in units of [boys] per [girl]..
    '''
    n_girls = fams
    n_boys = fams*approxBoysSeries(fams)
    return  n_boys / n_girls


def approxExpectedVal(N: int, p: float) -> float:
    '''
    Parameters
    ----------
    N : int
        Number of families to consider.
    p : float
        Probability of a success.

    Returns
    -------
    float
        The N-term approximation of the expected value, E[X], of a Geometric 
        random variable X. Should be about 1/p.
    '''
    return sum(k*p*(1-p)**(k-1) for k in range(1,N+1))


def estimateRatioVer2(N: int, p_val: float) -> float:
    '''
    Parameters
    ----------
    N : int
        Number of families to consider.
    p_val : float
        Probability of a success.

    Returns
    -------
    float
        The approximate fraction of boys divided by the approximate fraction 
        of girls taken from N trials of a Geometric random variable. Not as
        accurate.
    '''
    ratio = np.inf         # represents no girls realized
    while ratio == np.inf: # keep drawing N samples until there is one success        
        z = np.random.geometric(p_val, size=N)
        frac_boys = sum(z > 1) / N
        frac_girls = sum(z == 1) / N
        ratio = frac_boys / frac_girls
    return ratio


if __name__ == "__main__":
    n = 1
    print(estimateRatio(n))
    print(estimateRatioVer2(n, 0.5))