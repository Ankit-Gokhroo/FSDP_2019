# -*- coding: utf-8 -*-
"""
Created on Mon Jun 17 17:56:54 2019

@author: Ankit Gokhroo
"""


"""
Code Challenge ( Pie Chart )
  Name: 
    university data
  Filename: 
    university_pie.py
  Problem Statement:
    Write a python code and make a pie chart using following conditions:
        1.Read data from csv (University_data.csv)
        2.count GRE score for each university and plot a pie chart
        3.explode minimun gre score university
"""

import csv
university_data = {}
with open('University_data.csv','rt') as uni:
    reader = csv.reader(uni,delimiter = ',')
    next(reader)
    for i in reader:
        if i[0] in university_data:
            university_data[i[0]] += int(i[1])
        else:
            university_data[i[0]] = int(i[1])

a=university_data.keys()
a=list(a)

b=university_data.values()
b=list(b)

import matplotlib
from matplotlib import pyplot as plt

import matplotlib.pyplot as plt
#plt.style.use('fivethirtyeight')

explode = (0, 0, 0, 0,0.1)

colors =['blue','red','yellow','green','pink']

plt.pie(b,labels=a,explode=explode, colors=colors, wedgeprops={'edgecolor':'black'},autopct='%1.1f%%')

plt.show()
