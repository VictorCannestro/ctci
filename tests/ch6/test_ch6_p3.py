# -*- coding: utf-8 -*-
"""
Created on Tue Jan 12 17:27:05 2021

@author: Victor Cannestro
"""
import pytest
from typing import Tuple
from src.ch6.p3_dominos import Domino, Board


class TestDomino(object):
    ids = [1,2,30]
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