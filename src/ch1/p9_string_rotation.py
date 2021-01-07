# -*- coding: utf-8 -*-
"""
Assume you have a method `isSubstring` which checks if one word is a substring
of another. Given two strings, `s1` and `s2`, write code to check if `s2` is a 
rotation of `s1` using only one call to `isSubstring` (e.g. "waterbottle" is a
rotation of "erbottlewat").

@author: Victor Cannestro
"""

def isRotation(s1,s2):
    '''
    Parameters
    ----------
    s1 : str
        Input string for comparison.
    s2 : str
        Input string for comparison.

    Returns
    -------
    bool.
        The determination of whether if `s2` is a rotation of `s1`.
        E.g. "waterbottle" is a rotation of "erbottlewat"
    '''
    if len(s1) != len(s2):
        return False
    # Test for 0th order rotation first
    shifted = s2             
    for i in range(len(s1)):
        if s1 == shifted:
            return True
        else:
            # Rotate to the left by 1 char
            shifted = s2[i:] + s2[:i] 
    return False


def isRotationVer2(s1,s2):
    '''
    Assumes the existence of a method `isSubstring` which checks if one 
    word is a substring of another. Implementation uses only one call to 
    `isSubstring`. In Python we can just use the `in` keyword.
    E.g. 
        "waterbottle" is in "erbottlewat" + "erbottlewat""
    '''
    if len(s1) != len(s2):
        return False
    elif len(s1) == 0:
        return False
    elif s2 in s1+s1:
        return True
    else:
        return False
    

if __name__ == "__main__":
    s1 = "oobleck"
    s2 = "bleckoo"
    print(isRotation(s1,s2))
    print(isRotationVer2(s1,s2))