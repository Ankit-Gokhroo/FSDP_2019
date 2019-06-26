# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 17:45:08 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Character Frequency
  Filename: 
    frequency.py
  Problem Statement:
    This program accepts a string from User and counts the number of characters (character frequency) in the input string.  
  Input: 
    www.google.com
  Output:
    {'c': 1, 'e': 1, 'g': 2, 'm': 1, 'l': 1, 'o': 3, '.': 2, 'w': 3}
"""


str1=input('enter the string')


dict1={}
for i in str1:
    if i in dict1:
        dict1[i]=dict1[i]+1
    else:
        dict1[i]=1


      
        

            
    
 






dict1['jhjh']=87