# -*- coding: utf-8 -*-
"""
Implement a method to perform basic string compression using the counts of 
repeated characters. For example, the string "aabcccccaaa" would become 
"a2b1c5a3". If the "compressed" string would not become smaller than the 
original string, your method should return the original string. You can assume
the string has only uppercase and lowercase letters (a-z).

@author: Victor Cannestro
"""

def basicCompression(string: str) -> str:
    '''
    Parameters
    ----------
    string : str
        Input string for processing.

    Returns
    -------
    str
        A "compressed" string where letters are coded as frequecies
        after the first instance.
    Example:
        >>basicCompression("oooof")
        "o4f1"
    '''
    N = len(string)
    if N == 0:
        return string
    idx = 0
    idxCount = {0:1}
    prevChar = string[0]
    for i in range(1, N):
        if string[i] == prevChar:
            idxCount[idx] += 1
        else:
            prevChar = string[i]
            idx = i
            idxCount.setdefault(idx, 1)
    compressed = "".join([f"{string[k]}{v}" for k,v in idxCount.items()]) 
    if len(compressed) < N:
        return compressed
    else:
        return string


if __name__ == "__main__":
    s1 = "ooooooorf"
    print(basicCompression(s1))