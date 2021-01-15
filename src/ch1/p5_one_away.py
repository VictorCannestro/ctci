# -*- coding: utf-8 -*-
"""
There are three types of edits that can be performed on strings: insert a
character, remove a character, or replace a character. Given two strings, 
write a function to check if they are one edit (or zero edits) away.

@author: Victor Cannestro
"""

def checkForInsertion(s1: str, s2: str, length: int) -> bool:
    for i in range(length):
        temp = s1[:i] + s1[i+1:]
        if temp == s2:
            return True
    return False

def oneEditAway(str1: str, str2: str) -> bool:
    '''
    Parameters
    ----------
    str1 : str
        Input string for comparison.
    str2 : str
        Input string for comparison.

    Returns
    -------
    bool
        Determination of whether the input strings are one edit (or zero 
        edits) away. Will return True if both strings are empty.
    '''
    len1, len2 = len(str1), len(str2)
    if str1 == str2:           
        return True
    # One string has 2+ more characters
    elif abs(len1 - len2) > 1: 
        return False
    # Case of replacement edit
    elif len1 == len2:        
        for i in range(len1 - 1):
            temp1 = str1[:i] + str1[i+1:]
            temp2 = str2[:i] + str2[i+1:]
            if temp1 == temp2:
                return True
        return False
    # Case of removal/insertion
    elif len1 > len2:          
        return checkForInsertion(str1, str2, len1)
    # len1 < len2 
    else:                      
        return checkForInsertion(str2, str1, len2)

if __name__ == "__main__":
    s1 = "soup"
    s2 = "sub"
    print(oneEditAway(s1,s2))