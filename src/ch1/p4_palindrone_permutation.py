# -*- coding: utf-8 -*-
"""
Given a string, write a function to check if it is a permutation of a 
palindrone. A palindrone is a word or phrase that is the same forwards and 
backwards. A permutation is a rearrangement of letters. The palindrone does
not need to be limited to just dictionary words. You can ignore casing and 
non-letter characters.

@author: Victor Cannestro
"""
from itertools import permutations

def getUniquePerms(inputlist):
    # THIS IS A BOTTLENECK
    perms = permutations(inputlist) # n! elements
    return [*set(perms)] # discard redundant elements

def isPalindrone(string):
    if string == string[::-1]:
        return True
    return False
    
def isPermutedPalindrone(string):
    '''
    Parameters
    ----------
    string : str
        input string.

    Returns
    -------
    bool
        The determination of whether string is a permutation of a 
        palindrone.
    '''
    if len(string) == 0:
        return False   
    perms = getUniquePerms(string)
    for i in perms:
        if isPalindrone("".join(i)) == True:
            return True
    return False

if __name__ == "__main__":
    s = "wow"
    print(isPermutedPalindrone(s))