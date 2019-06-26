# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:37:52 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Romeo and Juliet
  Filename: 
    romeo.py
  Problem Statement:
    Let’s start with a very simple file of words taken from the text of 
    Romeo and Juliet. (romeo.txt)
    We will write a Python program to read through the lines of the file
    break each line into a list of words
    and then loop through each of the words in the line,
    and count each word using a dictionary.    
"""


empty_list=[]
dict1={}
with open ("romeo2.txt",mode="rt") as wf:
    content=wf.read().split()
    empty_list.append(content)
    for i in empty_list:
        if i in dict1.keys():
            dict1[i]+=1
        else:
            dict1[i]=1
    
    
print(dict1)    

    