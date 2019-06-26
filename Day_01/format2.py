# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 19:00:32 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Formatted String
  Filename: 
    format2.py
  Problem Statement:
    Write a program to print the output in the given format. 
    Take input from the user. 
  Hint:
    Try to serach for some function in the str class using help() and dir()
  Input:
    Welcome to Pink City Jaipur
  Output:
    Welcome*to*Pink*City*Jaipur
"""

x=input('enter the string')

dir(str)
help(str.replace)
updated_string=x.replace(' ','*')
 
print(updated_string)

