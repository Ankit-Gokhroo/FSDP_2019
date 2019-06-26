# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 16:30:37 2019

@author: Ankit Gokhroo
"""

"""
Code Challenge
  Name: 
    Supermarket
  Filename: 
    supermarket.py
  Problem Statement:
    You are the manager of a supermarket. 
    You have a list of items together with their prices that consumers bought on a particular day. 
    Your task is to print each item_name and net_price in order of its first occurrence. 
    Take Input from User  
  Hint: 
    item_name = Name of the item. 
    net_price = Quantity of the item sold multiplied by the price of each item.
    try to use new class for dictionary : OrderedDict
  Input:
    BANANA FRIES 12
    POTATO CHIPS 30
    APPLE JUICE 10
    CANDY 5
    APPLE JUICE 10
    CANDY 5
    CANDY 5
    CANDY 5
    POTATO CHIPS 30
  Output:
    BANANA FRIES 12
    POTATO CHIPS 60
    APPLE JUICE 20
    CANDY 20

"""

list1 = []
while True:
    user_input = input("Enter values >")
    
    #append this entry to other data structure
    list1.append(user_input)
    
    if not user_input:
        break
dict1={}
list1.pop()
d=[]
e=[]


for i in list1:
    a=i.split()
    e.append(a[-1])
    b =' '.join(a[:-1])
    d.append(b)
    
    
dd= dict(zip(d, e))


