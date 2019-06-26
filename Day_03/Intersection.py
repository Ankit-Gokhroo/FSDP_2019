# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:14:12 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Intersection
  Filename: 
    Intersection.py
  Problem Statement:
    With two given lists [1,3,6,78,35,55] and [12,24,35,24,88,120,155]
    Write a program to make a list whose elements are intersection of the above given lists.  
"""


a=[1,3,6,78,35,55]
b=[12,24,35,24,88,120,155]
c=[]
for i in a:
    if i in b:
        c.append(i)
    else:
        pass
    
print(c)   