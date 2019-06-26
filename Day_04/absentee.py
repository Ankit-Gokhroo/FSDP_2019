# -*- coding: utf-8 -*-
"""
Created on Thu Jun  6 16:14:48 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Create a list of absentee
  Filename: 
    absentee.py
  Problem Statement:
    Make a program that create a file absentee.txt
    The program should take max 25 students name one by one
    When the user enter a blank line, it should terminate the input
    Store all the name of students in the file    
    Once all the students names have been entered, it should display the list
    
"""

with open ("absentee.txt",mode="wt") as wf:
    a=1
    while a<=25:
        a=a+1
        student_name = input("Enter name of student >")
        if len(student_name) != 0:
            
            wf.write(student_name + "\n")
        else:
            
            break
    
    