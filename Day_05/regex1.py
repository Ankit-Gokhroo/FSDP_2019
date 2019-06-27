# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 10:43:44 2019

@author: Ankit Gokhroo
"""

"""

Code Challenge
  Name: 
    Regular Expression 1
  Filename: 
    regex1.py
  Problem Statement:
    You are given a string N. 
    Your task is to verify that N is a floating point number.
    Take Input From User

    In this task, a valid float number must satisfy all of the following 
    requirements:  
   
    Number can start with +, - or . symbol.
  Hint: 
    Using Regular Expression 
  Input:
    4  
    4.000
    -1.00
    +4.54
  Output:
    False
    True
    True
    True
"""
list1=[]
while True:
    user_input = input("Enter the value >")
    
    #append this entry to other data structure
    list1.append(user_input)
    
    if not user_input:
        break

import re

for i in list1:
    print(i)
    if re.findall(r'^[+-]?\d*\.\d*',i):
        print ('true')
        
    else:
        print ('false')
    
    
