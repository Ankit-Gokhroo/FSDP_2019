# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:53:37 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Space Seperated data
  Filename: 
    space_numpy.py
  Problem Statement:
    You are given a 9 space separated numbers. 
    Write a python code to convert it into a 3x3 NumPy array of integers.
  Input:
    6 9 2 3 5 8 1 5 4
  Output:
      [[6 9 2]
      [3 5 8]
      [1 5 4]]
  
"""

import numpy as np

a=input('enter 9 no. by space sepearted')
b=a.split( )
x=np.array(b,dtype = np.int8)
b=x.reshape(3,3)
print(b)

