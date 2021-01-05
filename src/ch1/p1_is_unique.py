# -*- coding: utf-8 -*-
"""
Implement an algorithm to determine if a string has all unique characters.
What if you cannot use additional data structures?

@author: Victor Cannestro
"""
def allUnique(string):
    '''
    Input:
        string (str): the string to be analyzed 
    Output:
        (bool)
    '''
    if type(string) != str:
        raise TypeError("Must input a string")
    elif len(string) == 0:
        return False
    
    unique = set(string)
    return len(unique) == len(string)


def allUniqueVer2(string):
    '''
    Input:
        string (str): the string to be analyzed 
    Output:
        (bool)
    '''
    if type(string) != str:
        raise TypeError("Must input a string")
    elif len(string) == 0:
        return False        
    
    n = len(string)
    for i in range(n):
        temp = string[i]
        for j in range(n):
            if string[j]==temp and i!=j:
                return False
    return True
        
if __name__ == "__main__":
    strings = ["Python is cool",""]
    for string in strings:
        print(allUnique(string))
        print(allUniqueVer2(string))