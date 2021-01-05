# -*- coding: utf-8 -*-
"""
Given two strings, write a method to decide if one is a permutation of the 
other.

@author: Victor Cannestro
"""

def isPermutation(str1, str2):
    '''
    Parameters
    ----------
    str1 : str
        An input string.
    str2 : str
        An input string.

    Returns
    -------
    bool
        Whether str1 is a permutation of str2 or vice versa. If either string
        is empty, "", return False.
    '''
    if len(str1) != len(str2):
        return False
    
    s1, s2 = set(str1), set(str2)
    if s1 == s2 and len(s1) != 0:
        return True
    return False

if __name__ == "__main__":
    s = "Cabbage soup"
    print(isPermutation(s,s))