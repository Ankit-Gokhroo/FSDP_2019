# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 15:54:18 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    weeks
  Filename: 
    weeks.py
  Problem Statement:
    Write a program that adds missing days to existing tuple of days
  Input: 
    ('Monday', 'Wednesday', 'Thursday', 'Saturday')
  Output:
    ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
"""


#a=input('enter no. of days seperated by comma')
#b=a.split(',')
#c=tuple(b)




day_fix=('monday', 'wednesday', 'thursday', 'saturday')

complete_week_days=(day_fix[0],)+('tuesday',)+(day_fix[2],)+(day_fix[3],)+('friday',)+(day_fix[3],)+('sunday',)