# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 11:22:11 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Duplicate
  Filename: 
    duplicate.py
  Problem Statement:
    With a given list [12,24,35,24,88,120,155,88,120,155]
    Write a program to print this list after removing all duplicate values 
    with original order reserved  
"""

a=[12,24,35,24,88,120,155,88,120,155]
b=[]

for i in a:
    if i in b:
        pass
    else:
        b.append(i)

