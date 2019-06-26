# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 11:15:18 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Bricks
  Filename: 
    bricks.py
  Problem Statement:
    We want to make a row of bricks that is target inches long. 
    We have a number of small bricks (1 inch each) and big bricks (5 inches each). 
    Make a function that prints True if it is possible to make the exact target 
    by choosing from the given bricks or False otherwise. 
    Take list as input from user where its 1st element represents number of small bricks, 
    middle element represents number of big bricks and 3rd element represents the target.
  Input: 
    2, 2, 11
  Output:
    True
"""


a=(input('enter the 3 no.'))
alist=a.split()

def target(alist):
    if int(alist[0])*1 + int(alist[1])*5 >= int(alist[2]):
        return True
    else:
        return False
    
target(alist)    