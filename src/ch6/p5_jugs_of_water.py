# -*- coding: utf-8 -*-
"""
You have a five-quart jug, a three-quart jug, and an unlimited supply of water
(but no measuring cups). How would you come up with exactly four quarts of 
water? Note that the jugs are oddly shaped, such that filling up exactly
"half" of the jug would be impossible.

    ANSWER:
        
        Step 1: Fill the 5 quart jug and leave the 3 quart jug empty.
        
                State: 5 quart jug @ 5qrts
                       3 quart jug @ 0qrts
        
        Step 2: Pour from the 5 quart into the 3 quart until the 3 quart jug 
                is full.
                
                State: 5 quart jug @ 2qrts
                       3 quart jug @ 3qrts
                       
        Step 3: Dump out the contents of the 3 quart jug.
        
                State: 5 quart jug @ 2qrts
                       3 quart jug @ 0qrts
                       
        Step 4: Pour the contents of the 5 quart jug into the 3 quart jug.
                
                State: 5 quart jug @ 0qrts
                       3 quart jug @ 2qrts
                       
        Step 5: Fill up the 5 quart jug.
        
                State: 5 quart jug @ 5qrts
                       3 quart jug @ 2qrts
                      
        Step 6: Pour the contents of the 5 quart jug into the 3 quart jug. 
        
                State: 5 quart jug @ 4qrts <--- answer achieved!
                       3 quart jug @ 3qrts

@author: Victor Cannestro
"""

if __name__ == "__main__":
    print("Read the docstring :)")