# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 15:50:04 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    copy command
  Filename: 
    copy.py
  Problem Statement:
    Make a program that create a copy of a file    
"""



with open ("first_file",mode="wt") as file:
    file.write('ankit')
    
    
with open ("first_file",mode="rt") as rf:
    with open ("second_file",mode="wt") as wf:
        for line in rf:
            wf.write(line)
            

with open ("third_file",mode='wt') as ef:
    pass
