# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 18:11:53 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Styling of String
  Filename: 
    style.py
  Problem Statement:
    Convert to uppercase character
    Convert to lower character 
    Convert to CamelCase or TitleCase.
  Hint: 
    Try to find some function in the str class and see its help on how to use it.
    Using dir and help functions
  Input:
    Take the name as input from the keyboard. ( SyLvEsTeR )
"""

x=input('enter the name')
type(x)

dir(str)
help(str.lower)

lower_string=str.lower(x)

upper_string=str.upper(x)

title_string=str.title(x)

camel_string=str.capitalize(x)