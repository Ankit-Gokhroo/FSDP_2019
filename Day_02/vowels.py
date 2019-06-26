# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 16:52:57 2019

@author: Ankit Gokhroo
"""


"""
Code Challenge
  Name: 
    Vowels Finder
  Filename: 
    vowels.py
  Problem Statement:
    Remove all the vowels from the list of states  
  Hint: 
    Use nested for loops and in membership Operator
  Input:
    state_name = [ 'Alabama', 'California', 'Oklahoma', 'Florida']
  Output:
    ['lbm', 'Clfrn', 'klhm', 'Flrd']
    
"""

vowels=['a','e','i','o','u']


input_string = input("Enter a name of states seperated by space ")
state_name  = input_string.split()


for i in state_name:
    for j in i:
        if j in vowels:
            i=i.replace(j,'')
    print(i) 
    
    
    
    
    
    
    
    
  