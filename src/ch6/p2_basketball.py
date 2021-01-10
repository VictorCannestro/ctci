# -*- coding: utf-8 -*-
"""
You have a basketball hoop and someone says that you can play one of two games.

    - Game 1: You get one shot to make the hoop
    - Game 2: You get three shots and you have to make two of three shots

If p is the probability of making a particular shot, for which values of p 
should you pick one game or the other?

ANSWER:
    
    Let X_1 ~ Bernoulli(p) represent the chance of winning Game 1 and 
    X_2 ~ Binomial(3,p) represent the chance of winning Game 2. The events in 
    question are 
    
        A = {You make the shot}
        B = {You make at least 2 of 3 shots} 

    for Games 1 and 2, respectively. The calculation is done as follows:
        
        P[A] = p
        
        P[B] = P[{Make 2 shots} U {Make 3 shots}]
             = P[k=2] + P[k=3]
             = 3!/(2!(3-2)!) * p^2 * (1-p) + 3!/(3!(3-3)!) * p^3
             = 3p^2 - 2p^3
    
    and setting these equations equal to each other yields 3 zeros at 0, 0.5, 
    and 1. There, it does not matter which game is chosen. From the graph we 
    see that Game 1 is better if p < 0.5 and Game to is better if p > 0.5.
    
@author: Victor Cannestro
"""
import matplotlib.pyplot as plt
import numpy as np


p = np.arange(0, 1.01, 0.01)
f_bern = lambda x: p
f_bino = lambda x: 3*p**2*(1-p) + p**3 
zeros = (0, 0.5, 1)

plt.rcParams["figure.figsize"] = [12,9]
plt.rcParams.update({'font.size': 18})
plt.plot(p, 
         f_bern(p), 
         label=r"Game 1: $P[A] = p$")
plt.plot(p, 
         f_bino(p), 
         label=r"Game 2: $P[A] = 3p^2(1-p) + p^3$")
plt.scatter(zeros, 
            zeros, 
            facecolors='none', 
            edgecolors='k')
plt.title('Probability of Winning Game 1 vs Game 2')
plt.xlabel('Probability of Making a Shot')
plt.ylabel(r'$P[A]$')
plt.legend()
plt.grid(True)

if __name__ == "__main__":
    plt.savefig("Prob_6_2")
    plt.show()