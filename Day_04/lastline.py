# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 17:26:58 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Last Line
  Filename: 
    lastline.py
  Problem Statement:
    Ask the user for the name of a text file. 
    Display the final line of that file.
    Think of ways in which you can solve this problem, 
    and how it might relate to your daily work with Python.
"""


with open ("absentee.txt",mode="rt") as wf:
    pass
    
input_filename=input('enter file name')


with open (input_filename+".txt",mode="rt") as rf:
    content=rf.readlines()[-1]
    
    print(content)
    