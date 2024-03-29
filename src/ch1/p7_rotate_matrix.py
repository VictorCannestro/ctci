# -*- coding: utf-8 -*-
"""
Given an image represented by an NxN matrix, where each pixel in the image is
represented by an integer, write a method to rotate the image by 90 degrees.
Can you do this in place?

@author: Victor Cannestro
"""
from typing import List


Vector = List[float]
Matrix = List[Vector]

def rotate(matrix: Matrix) -> Matrix:
    '''
    Parameters
    ----------
    matrix : list
        NxN list of lists where each element of the inner lists are integers 
        and N>=1.

    Returns
    -------
    list
    The same list rotated 90 CCW calculated in O(N**2) runtime.
    '''
    idx = 0
    N = len(matrix)
    rotated = [[] for i in range(N)]
    for col in range(N-1, -1, -1): # Traverse columns from Right to Left
        for row in range(N):       # Traverse each row
            rotated[idx].append(matrix[row][col])
        idx += 1
    return rotated


def rotateInPlace(matrix: Matrix) -> Matrix:
    '''
    Parameters
    ----------
    matrix : list
        NxN list of lists where each element of the inner lists are integers 
        and N>=1.

    Returns
    -------
    list
    The same list rotated 90 CCW calculated in O(N) runtime. Takes advantage
    of the observation that the minimum number of elements we can swap during
    a rotation in-place is 4 (since there are four corners).
    Example: Let N=4 and elements of the matrix be labeled x{row}{col}.
        i=0: 
            j=0: x00 <-- x03, x03 <-- x33, x33 <-- x30, x30 <-- x00
            j=1: x01 <-- x13, x13 <-- x32, x32 <-- x20, x20 <-- x01
            j=2: x02 <-- x23, x23 <-- x31, x31 <-- x10, x10 <-- x02
        i=1:
            j=1: x11 <-- x12, x12 <-- x22, x22 <-- x21, x21 <-- x11
    '''
    N = len(matrix)
    for i in range(round((N+1)/2)): # How many perimeter loops are there       
        for j in range(i, N-i-1): # Reduced size of inner perimeter loops
            # Store pre-swap values to make the substitutions
            x1 = matrix[i][j] 
            x2 = matrix[j][N-i-1]
            x3 = matrix[N-i-1][N-j-1]
            x4 = matrix[N-j-1][i]           
            # Swap "corners" to rotate 90 deg CCW
            matrix[i][j] = x2
            matrix[j][N-i-1] = x3
            matrix[N-i-1][N-j-1] = x4
            matrix[N-j-1][i] = x1          
    return matrix
    

if __name__ == "__main__":
    matrix = [[1,0,0,0],
              [0,1,0,0],
              [0,0,1,0],
              [0,0,0,1]]
    print(rotate(matrix))
    print(rotateInPlace(matrix))