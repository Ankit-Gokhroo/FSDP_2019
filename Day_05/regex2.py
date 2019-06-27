# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 11:34:14 2019

@author: Ankit Gokhroo
"""

"""

Code Challenge
  Name: 
    Regular Expression 2
  Filename: 
    regex2.py
  Problem Statement:
    You are given N email addresses. 
    Your task is to print a list containing only valid email addresses in alphabetical order.
    Valid email addresses must follow these rules:

    It must have the username@websitename.extension format type.
    The username can only contain letters, digits, dashes and underscores.
    The website name can only have letters and digits.
    The minimum length is 2 and maximum length of the extension is 4. 
  Hint: 
    Using Regular Expression 
  Input:
    lara@hackerrank.com
    brian-23@hackerrank.com
    britts_54@hackerrank.com
  Output:
    ['brian-23@hackerrank.com', 'britts_54@hackerrank.com', 'lara@hackerrank.com']

"""

list1=[]
list2=[]
while True:
    user_input = input("Enter the value >")
    
    #append this entry to other data structure
    list1.append(user_input)
    
    if not user_input:
        break
list1.pop()
import re

for i in list1:
    print(i)
    if re.findall(r'^\w+[_-]?\d*\@\w*\.[a-z]{2,4}',i):
        
        print ('true')
        r = re.findall(r'^\w+[_-]?\d*\@\w*\.[a-z]{2,4}',i)
        list2.extend(r)
        
    else:
        print ('false')
        

ss=sorted(list2)

#results = re.findall(r'^\w*\@\w*\.[a-z]{2,4}','ankit44@sdsd.com')
#print(results)     
    
    
