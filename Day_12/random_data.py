# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 16:05:03 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Random Data
  Filename: 
    random_data.py
  Problem Statement:
    Create a random array of 40 integers from 5 - 15 using NumPy. 
    Find the most frequent value with and without Numpy.
  Hint:
      Try to use the Counter class and also bincount
      
      
"""

import numpy as np
x = np.random.randint(5,15,40)

from scipy import stats
stats.mode(x)

