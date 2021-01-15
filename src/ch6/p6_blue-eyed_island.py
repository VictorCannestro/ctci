# -*- coding: utf-8 -*-
"""
A bunch of people are living on an island, when a visitor comes with a strange
order: all blue-eyed people must leave the island as soon as possible. There
will be a flight out at 8:00pm every evening. Each person can see everyone 
else's eye color, but they do not know their own (nor is anyone allowed to 
tell them). Additionally, they do not know how many people have blue eyes, 
although they do know that at least one person does. How many days will it 
take the blue-eyed people to leave?

ANSWER:
    
    The most important pieces of information given are that no resident is 
    allowed to tell another the other's eye color and that residents don't 
    know their own eye color. This creates some uncertainty and the only 
    thing any individual resident can be sure of is the status of every other 
    residents' eye color. (We'll assume implicitly assume them to be rational,
    cooperative agents). 
    
    Best Case: Exactly 1 person has blue eyes (BEs). From their perspective, 
               no one else has BEs. (From everyone else's persepective there 
               there is one person with BEs). They know that at least 1 person
               has BEs so it must be them and they leave that night. 
               Afterwards, the other residents would know that they don't have
               BEs. 
               
    If exactly 2 people have BEs things are a little different. From each of 
    their perspectives 1 person has BEs. (From everyone else's persepective 
    there are 2 people with BEs). However, neither know if their own eyes are
    blue. They do know that if only 1 person has BEs that person would leave 
    that night. Thus, they wait until the next day. If no one left the night 
    before, they would know that they have BEs and leave that night.
    Afterwards, the other residents would know that they don't have BEs.
    .
    .
    .
    Worst Case: All n people have BEs. From each of their perspectives n-1 
                people have BEs. However, none of them know if their own eyes 
                are blue. They do know that if only 1 person has BEs that 
                person would leave that night; if 2, those 2 would leave after
                2 nights and so on. Thus, they wait n days. If no one has left
                by then, they would know that they have BEs and leave that 
                night along with everyone else. Afterwards, the island would 
                be abandoned.

@author: Victor Cannestro
"""

if __name__ == "__main__":
    print("Read the docstring :)")