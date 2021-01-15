# -*- coding: utf-8 -*-
"""
Write a method to replace all spaces in a string with '%20'. You may assume 
that the string has sufficient space at the end to hold the additional 
characters, and that you are given the "true" length of the string. (Note: If
implementing in Java, please use a character array so that you can perform
this operatio in place.)

@author: Victor Cannestro
"""

def urlify(string: str) -> str:
    '''
    Parameters
    ----------
    string : str
        Input string.

    Returns
    -------
    str
        a string in which '%20' has replaced all the spaces in it
    '''
    chars = string.split()
    return "%20".join(chars)


if __name__ == "__main__":
    s = "Cabbage soup"
    print(urlify(s))