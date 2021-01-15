# -*- coding: utf-8 -*-
"""
ANSWER:
    
    Let X ~ Geometric(p) where p = 0.5 and let N = the # of families present. 
    We'll also assume each birth and family are independent. The PMF of a 
    Geometric random variable is
        
    p_X[k] = p*(1-p)**(k-1) for k = 1,2,3,...
           = 1/2**k        since there's an equal likelihood of either outcome 
    
    where p is the probability of success. Here we know that a family stops
    having children once they have a girl, so there will be exactly 1 girl per
    family, totalling N girls if we count all the families. Intuitively, 
    because of this process we can expect the gender ratio of the new 
    generation to be skewed towards boys for small numbers of families, but 
    balance out for large numbers of families. 
    
    We can expect 50% of the families to have 1 girl (G) and 0 boys (B) since 
    the probability of the first success is p = 1/2. Next, we can expect 25% 
    of the families to have 1 girl (G) and 1 boy (B), then 12.5% to have 1G 
    and 2Bs, etc. Mapping the outcomes in the sample space S = {B,G} to a 
    numerical space S_X = {0,1} we can define random sequences. Let's 
    enumerate the possiblities in a table:

    Outcome |   Vector    | Probability
    --------|-------------|------------
    G       | (1)         |    1/2
    BG      | (0,1)       |    1/4
    BBG     | (0,0,1)     |    1/8
    BBBG    | (0,0,0,1)   |    1/16
    BBBBG   | (0,0,0,0,1) |    1/24
    .
    .
    .
    B...BG  | (0,...,0,1) |    1/2**N
    
    Thus, the number of boys (with a corresponding probability weight) is 
    proportional to:
    
    |Bs|/N = (0)/2 + (1)/4 + (2)/8 + (3)/16 + ... + (N-1)/2**N
           = sum( k/2**(k+1) for k in range(0,N) )
           = p_X[1]*(0) + p_X[2]*(1) + p_X[3]*(2) + ... + p_X[N]*(N-1) 
           = sum( (k-1)*p_X[k] for k in range(1,N+1) )
           = sum( (k-1)*p*(1-p)**(k-1) for k in range(1,N+1) )
           = sum(k*p*(1-p)**(k-1) for k in range(1,N+1)) - sum( p*(1-p)**(k-1) for k in range(1,N+1) )
           = E[X] - 1     in the limit as N -> oo
           = 1/p - 1.
    
    Thus the gender ratio as the number of families N -> oo (goes to infinity)
    is: 
    
    N / (N*|Bs|) = 1 / (1/p - 1) 
                 = p / (1 - p)
                 = 0.5 / 0.5
                 = 1
    
    where the expressions in the denominator are the expected value of X 
    (i.e. 1/p) and the sum of X over all space (i.e. 1). Hence, in the finite
    population, there should be 50% Boys and 50% girls. 

@author: Victor Cannestro
"""
import pytest
import numpy as np
from src.ch6.p7_the_apocalypse import approxExpectedVal, approxBoysSeries, estimateRatio, estimateRatioVer2


class TestMethod(object):
    families = [1, 6, 1000]
    weightedProbs = [0.25, 0.9375, 1]
    tols = [3, 0.2, 1e-6] 
    
    # Done    
    @pytest.mark.parametrize("fams, tol", zip(families, tols))
    def test_approxExpectedVal(self, fams, tol):
        ans = 2 # 1/p = 1/(1/2)
        calc = approxExpectedVal(fams, 0.5)
        message = f"Expected {ans} but got {calc}"
        assert pytest.approx(calc, tol) == ans, message

    # Done
    @pytest.mark.parametrize("families, ans", zip(families, weightedProbs))
    def test_approxBoysSeries(self, families, ans):
        calc = approxBoysSeries(families)
        message = f"Expected {ans} but got {calc}"
        assert pytest.approx(calc) == ans, message

    # Done
    @pytest.mark.parametrize("fams, tol, ans", zip(families, tols, weightedProbs))
    def test_approxNumberOfBoys(self, fams, tol, ans):
        calc1 = approxExpectedVal(fams, 0.5) - 1
        calc2 = approxBoysSeries(fams)
        message = f"Expected the calculations to be about the same but got:\n{calc1}\n{calc2}"
        assert pytest.approx(calc1, tol) == ans, message
        assert ans == pytest.approx(calc2, tol), message

    # Done 
    @pytest.mark.parametrize("fams", families)       
    def test_estimateRatio(self, fams):
        ans = 1
        calc = np.ceil(estimateRatio(fams))
        message = f"Expected {ans} but got {calc}"
        assert calc == ans, message
        
    # Done 
    def test_estimateRatioVer2(self):
        ans = 1
        calc = estimateRatioVer2(10000, 0.5)
        message = f"Expected {ans} but got {calc}"
        assert pytest.approx(calc, 0.2) == ans, message        