# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:33:25 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    String Handling
  Filename: 
    stringhand.py
  Problem Statement:
    Take first and last name in single command from the user and print  
    them in reverse order with a space between them, 
    find the index using find/index function and then print using slicing concept of the index
  Input:
      Sylvester Fernandes
  Output: 
      Fernandes Sylvester 
"""

full_name=input('enter first name and last name')

dir(str)
help(str.index)

space_found=full_name.index(' ')
reverse_full_name=full_name[6:]+' '+full_name[:space_found]

print(reverse_full_name)