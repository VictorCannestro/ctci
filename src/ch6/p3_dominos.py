# -*- coding: utf-8 -*-
"""
There is an 8x8 chessboard in which two diagonally opposite corners have been
cut off. You are given 31 dominos, and a single domino can cover exactly two 
squares. Can you use the 31 dominos to cover the entire board? Prove your
answer.
               
@author: Victor Cannestro
"""
from typing import Tuple


class Domino:
    def __init__(self, id: int):
        if id < 0:
            raise ValueError("Domino ID must be non-negative")
        self.isPlaced = False
        self.ID = id
        self.position = ()

    def __str__(self) -> str:
        return str(f"Domino {self.ID}")
    
    def __repr__(self) -> str:
        return f"Domino(ID={self.ID}, isPlaced={self.isPlaced}, position={self.position})"
    
    def setPosition(self, newPosition: Tuple):
        self.isPlaced = not self.isPlaced
        self.position = newPosition
        
    def getPosition(self) -> Tuple:   
        return self.position
    
    def getIsPlaced(self) -> bool:
        return self.isPlaced
    
    def getID(self) -> int:
        return self.ID
        
    
class Board:
    dominoIDs = []
    dominosPlaced = 0
    
    def __init__(self, n: int):
        '''Constructs an alternating nxn grid of 0s and 1s'''
        self.grid = [['[ B ]' if (i+j)%2==0 else '[ W ]' for j in range(n)] for i in range(n)]
        self.grid[0][0] = '[   ]'
        self.grid[n-1][n-1] = '[   ]'
        
    def __str__(self) -> str:
        s = ''
        for i in self.grid:
            for element in i:
                s += element
            s += '\n'
        return s
    
    def __repr__(self) -> str:
        info = f"Board(n={len(self.grid)}, dominosPlaced={self.dominosPlaced})"
        return info
      
    def addDomino(self, domino, position: Tuple):
        p1, p2 = position
        dom_id = domino.getID()
        self.dominoIDs.append(dom_id)
        self.dominosPlaced += 1
        extra = " " if dom_id < 10 else ""
        domino.setPosition(position)
        for p in position:
            self.grid[p[0]][p[1]] = f"[ {dom_id}{extra}]"
            
    def getOpenPositions(self):
        pass
    
    def getDominosPlaced(self):
        return self.dominosPlaced

        
class Controller:
    def __init__(self):
        pass
    
    
        
        
if __name__ == "__main__":
    b = Board(8)
    print(b)
    
    d1 = Domino(1)
    d2 = Domino(2)
    print(d1)
    print(d2)
    
    b.addDomino(d1, ((0,1),(0,2)))
    b.addDomino(d2, ((1,0),(1,1)))
    print(b)
    print(repr(d1))