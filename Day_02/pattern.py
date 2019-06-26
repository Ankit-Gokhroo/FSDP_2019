# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:16:24 2019

@author: Ankit Gokhroo
"""


"""
Code Challenge
  Name: 
    Pattern Builder
  Filename: 
    pattern.py
  Problem Statement:
    Write a Python program to construct the following pattern. 
    Take input from User.  
  Input: 
    5
  Output:
    Below is the output of execution of this program.
      * 
      * * 
      * * * 
      * * * * 
      * * * * * 
      * * * * 
      * * * 
      * * 
      * 
"""

j=int(input('enter a number'))

i=0
while i<j:
    print('* '*i)
    i=i+1
while i>0:
    print('* '*i)
    i=i-1

    
        
    
   
    