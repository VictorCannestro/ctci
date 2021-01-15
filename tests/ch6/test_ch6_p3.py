# -*- coding: utf-8 -*-
"""
ANSWER:
    
    There are now 30 black tiles and 32 white tiles (or vice versa if the 
    other set of corners is considered). The 31 dominos we have available can
    cover up to 62 tiles on the board, assuming the board is normal and we 
    place them wisely in a configuration that leaves no spaces in between
    dominos. With the 2 tiles missing, there are 62 open tiles on board. 
    
    There are 3 starting/ending configurations by the missing corners if we 
    try to cover all the tiles without leaving spaces:
    
        [   ][ 1 ][ 1 ]...
        [ 2 ][ B ][ W ]...
        [ 2 ][ W ][ B ]...
    
        [   ][ 1 ][ B ]...
        [ 2 ][ 1 ][ W ]...
        [ 2 ][ W ][ B ]...
        
        [   ][ 1 ][ 1 ]...
        [ 2 ][ 2 ][ W ]...
        [ B ][ W ][ B ]...
        
    where dominos are represented as individual integers in a row/col.
    
    Best Case: We can fit at most 30 dominos on the board with 2 tiles left 
               open after following an efficient configuration. (So called 
               proof by picture).
              
    Claim: On an NxN checkered board where N is an even natural number (i.e. 
           2,4,6,8,...) there will always be 2 squares left uncovered if any
           two diagonal corners are cut off and the dominos can cover 2 tiles
           in either a row or column each.
                      
           2x2 Case             4x4 Case
           [   ][ W ]           [   ][ 1 ][ 1 ][ 4 ]
           [ W ][   ]           [ 2 ][ 2 ][ 3 ][ 4 ]
                                [ 5 ][ 5 ][ 3 ][ W ]
                                [ 6 ][ 6 ][ W ][   ]

@author: Victor Cannestro
"""
import pytest
from typing import Tuple
from src.ch6.p3_dominos import Domino, Board


class TestDomino(object):
    ids = [1, 2, 30]
    doms = [Domino(i) for i in ids]
    positions = [((0,1),(0,2)), ((1,0),(1,1)), ((4,4),(4,5))]
        
    @pytest.mark.xfail
    def test___init__(self):
        with pytest.raises(ValueError) as exception_info: # store the exception
            d = Domino(-1)
        assert exception_info.match("Domino ID must be non-negative")
        
    @pytest.mark.parametrize("d_id, domino", zip(ids, doms))
    def test___str__(self, d_id: int, domino: Domino):
        ans = f"Domino {d_id}"
        calc = str(domino)
        message = f"Expected {ans} but got {calc}"
        assert ans == calc, message
        
    def test_getIsPlacedDefault(self):
        ans = False
        calc = Domino(1).getIsPlaced()
        message = f"Expected {ans} but got {calc}"
        assert ans == calc, message
        
    @pytest.mark.parametrize("d_id, domino", zip(ids, doms))
    def test_getID(self, d_id: int, domino: Domino):
        calc = domino.getID()
        message = f"Expected {d_id} but got {calc}"
        assert  d_id == calc, message
        
    def test_getPositionDefault(self):
        ans = ()
        calc = Domino(1).getPosition()
        message = f"Expected {ans} but got {calc}"
        assert ans == calc, message

    @pytest.mark.parametrize("position, domino", zip(positions, doms))    
    def test_setPosition(self, position: Tuple, domino: Domino):
        domino.setPosition(position)
        ans = position
        calc = domino.getPosition()
        message = f"Expected {ans} but got {calc}"
        assert ans == calc, message
        
        
class TestBoard(object):

    @pytest.mark.skip(reason="")
    def test___str__(self):
        assert False
        
    @pytest.mark.skip
    def test___repr__(self):
        assert False
        
    @pytest.mark.skip
    def test_addDomino(self):
        assert False
        
    @pytest.mark.skip
    def test_addDomino2(self):
        assert False
        
    @pytest.mark.skip
    def test_getOpenPositions(self):
        assert False