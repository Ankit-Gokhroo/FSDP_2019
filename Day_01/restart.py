# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:24:12 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Replacing of Characters
  Filename: 
    restart.py
  Problem Statement:
    In a hardcoded string RESTART, replace all the R with $ except the first occurrence and print it.
  Input:
    RESTART
  Output: 
    RESTA$T
"""

hardcoded_string='RESTART'
replace_string='R'+hardcoded_string[1:].replace('R','$')
print(replace_string)