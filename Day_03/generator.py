# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:46:24 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    generator
  Filename: 
    generator.py
  Problem Statement:
    This program accepts a sequence of comma separated numbers from user 
    and generates a list and tuple with those numbers.  
  Input: 
    2, 4, 7, 8, 9, 12
  Output:
    List : ['2', ' 4', ' 7', ' 8', ' 9', '12'] 
    Tuple : ('2', ' 4', ' 7', ' 8', ' 9', '122')
"""
a=input('enter values seperate by comma')

b=a.split(sep=',')
c=tuple(b)
print('List :', b)
print('Tuple :', c)

