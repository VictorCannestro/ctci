# -*- coding: utf-8 -*-
"""
You have a basketball hoop and someone says that you can play one of two games.

    - Game 1: You get one shot to make the hoop
    - Game 2: You get three shots and you have to make two of three shots

If p is the probability of making a particular shot, for which values of p 
should you pick one game or the other?

@author: Victor Cannestro
"""
import matplotlib.pyplot as plt
import numpy as np

N = 3
p = np.arange(0, 1.01, 0.01)
outcomes = []
for i in range(len(p)):
    x = sum(np.random.binomial(N, p) > 1)
    print(x)
    outcomes.append(x)
plt.hist( outcomes)
plt.xlabel('Probability of Making a Shot')
plt.ylabel('Probability')

if __name__ == "__main__":
    plt.show()