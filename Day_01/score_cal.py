# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 17:39:55 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Weighted Score Calculator
  Filename: 
    score_cal.py
  Problem Statement:
    Lets assume there are 3 assignments and 2 exams, each with max score of 100. 
    Respective weights are 10%, 10%, 10%, 35%, 35% . 
    Compute the weighted score based on individual assignment scores.  
  Hint: 
    weighted score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
"""

assignment_1=float(input('enter your marks of assignment1'))
assignment_2=float(input('enter your marks assignment2'))
assignment_3=float(input('enter your marks assignment3'))

exam_1=float(input('enter your marks exam1'))
exam_2=float(input('enter your marks exam2'))

weighted_score=(assignment_1+assignment_2+assignment_3) *0.1 + (exam_1 + exam_2) *0.35

