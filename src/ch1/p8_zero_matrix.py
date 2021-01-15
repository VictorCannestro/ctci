# -*- coding: utf-8 -*-
"""
Write an algorithm such that if an element in an MxN matrix is 0, its entire
row and column are set to 0.

@author: Victor Cannestro
"""
from typing import List


Vector = List[float]
Matrix = List[Vector]

def setZeros(matrix: Matrix) -> Matrix:
    '''
    Parameters
    ----------
    matrix : list
        An MxN matrix (i.e. a nested list).

    Returns
    -------
    matrix : list
        An MxN matrix such that if an element of the input matrix is 0, its 
        entire row and column are set to 0.
    '''
    idxs = set([])
    M, N = len(matrix), len(matrix[0])
    for row in range(M):
        if 0 not in matrix[row]: # O(N) lookup
            continue
        else:
            # Find indices of 0 elements and set nonzero row elements to 0
            for col in range(N):
                if matrix[row][col] == 0:
                    idxs.update({col})
                else:
                    matrix[row][col] = 0
    # Now we set the columns to 0 (if any)
    for row in range(M):
        for col in list(idxs):
            matrix[row][col] = 0
    return matrix

def setZerosVer2(matrix: Matrix) -> Matrix:
    pass


if __name__ == "__main__":
    matrix = [[1,0],
              [1,2],
              [1,3],
              [1,4]]
    print(setZeros(matrix))